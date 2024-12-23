from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .serializers import UsersSerializer, BoardSerializer
from .models import Users, Boards
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from .sudoku import Sudoku, KillerSudoku
import json
import copy
from django.http import JsonResponse


def index(request):
    """
    A function that creates a simple welcome page. Not seen by the users.
    Created when first initialized the Django project.
    """
    return HttpResponse("Hello, world. You are at the sudoku index.")


class UsersView(viewsets.ModelViewSet):
    """
    Class responsible for the pages that handle requests to the Users table.

    ATTRIBUTES:
        serializer_class: a serializer which is where the data from the frontend is stored.
                          See serializers.py for more information

    METHODS:
        signup_view: Handles signup process
        signin_view: Handles signin process
    """

    serializer_class = UsersSerializer


@api_view(["POST"])
def signup_view(request):
    """
    Handles the user signup process.

    This view function processes POST requests for user registration. It uses a
    serializer to validate and save the new user data. If the provided data is
    valid, it creates a new user and returns the user data with a 201 CREATED status.
    If the data is invalid, it prints the received data and errors, and returns the
    errors with a 400 BAD REQUEST status.

    Args:
        request (Request): The Django REST framework request object containing
                           the user data.

    Returns:
        Response: A Django REST framework response object. On successful user creation,
                  it returns the user data with a 201 CREATED status. On failure, it
                  returns the validation errors with a 400 BAD REQUEST status.
    """
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print("Received data:", request.data)
        print("Serializer errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def signin_view(request):
    """
    Handle the user signin process via POST request.

    Authenticates a user based on the provided email and password. It first checks if
    a user with the given email exists. If the user exists and the provided password
    matches the stored password hash, it returns a success response. Otherwise, it
    returns an unauthorized response.

    Parameters:
    request (Request): A Django REST framework Request object containing the user"s
                       email and password.
    Returns:
    Response: A Django REST framework Response object. Returns a success message with
              a 200 OK status if the authentication is successful. Returns an error
              message with a 401 UNAUTHORIZED status if the credentials are invalid.
    """
    email = request.data.get("email")
    password = request.data.get("pwd")
    try:
        user = Users.objects.get(email=email)
    except Users.DoesNotExist:
        return Response(
            {"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )

    if check_password(password, user.pwd):
        return Response({"message": "User authenticated"}, status=status.HTTP_200_OK)
    else:
        return Response(
            {"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class BoardView(viewsets.ModelViewSet):
    """
    Class responsible for the pages that handle requests to the Boards table.

    ATTRIBUTES:
        serializer_class: a serializer which is where the data from the frontend is stored.
                          See serializers.py for more information

    METHODS:
        get_game_by_difficulty: Used when user selects create a new game
        load_saved_game: Used when user wants to load a game they already saved
        save_game_state: Used whenever the game's state is updated
    """

    serializer_class = BoardSerializer


@api_view(["POST"])
def get_game_by_difficulty(request):
    """
    Handle the user create a new sudoku game process via POST request.

    It receives the user's chosen difficulty, style, and username. Then it createas
    a new sudoku game based on the chossen difficulty. Then it creates a new row in
    the Boards table containing all of its relevent information like the answer,
    status, and style. Once the new row is made, it returns the new game's inital
    state.

    Parameters:
    request (Request): A Django REST framework Request object containing the user's
                       username, chosen difficult, and chosen style.
    Returns:
    Response: A Django REST framework Response object. Returns a success message
              along with the newly created sudoku board data.
    """
    difficulty = request.data.get("difficulty")
    style = request.data.get("style")
    user = request.data.get("user")
    if style == "killer":
        game = KillerSudoku(difficulty)
    else:
        game = Sudoku(difficulty)
    status = game.sudoku_status()
    answer = copy.deepcopy(game)
    answer.solve_sudoku()
    board = Boards(
        state=str(game.board),
        initial=str(game.board),
        answer=str(answer.board),
        difficulty=difficulty,
        style=style,
        user=user,
        isFinished=status,
    )
    board.save()
    serializer = BoardSerializer(board)
    return Response(serializer.data)


@api_view(["GET"])
def load_saved_game(request):
    """
    Handle the user create a new sudoku game process via POST request.

    It receives the current user's username and style. Then it makes a query to
    the Boards table filtering all the rows for that username, that style, and
    who's progress is less than 100%. It then returns this query as a list of
    boards to the frontend.

    Parameters:
    request (Request): A Django REST framework Request object containing the user's
                       username and style of board.
    Returns:
    Response: A Django REST framework Response object. Returns a success message
              along with the array of all the sudoku board data that was requested.
    """
    try:
        username = request.query_params.get("username")  # Fetch the username parameter
        style = request.query_params.get("style")  # Fetch the style parameter

        # Filter based on username and style
        if style:
            boards = Boards.objects.filter(
                user=username, style=style, isFinished__lt=100.0
            )
        else:
            boards = Boards.objects.filter(user=username, isFinished__lt=100.0)

        if not boards.exists():
            return Response({"message": "No saved game found"}, status=404)

        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"message": f"Error: {str(e)}"}, status=500)


@api_view(["POST"])
def save_game_state(request):
    """
    Handle the user saving a sudoku game prgoress process via POST request.

    It receives the current sudoku board id and the new board state. Then it
    searches for the board row in the Boards table based on the board id. If it
    finds the board, it then updates both the progress field and the state to its
    new state. If it doesn't find it, it throws an error.

    Parameters:
    request (Request): A Django REST framework Request object containing the user's
                       username, chosen difficult, and chosen style.
    Returns:
    Response: A Django REST framework Response object. Returns a success message with
              a 200 OK status if the board was saved successfully. Returns an error
              message with a 404 status if the board was not found.
    """
    board_id = request.data.get("board_id")
    new_state = json.loads(request.data.get("state"))
    try:
        board = Boards.objects.get(id=board_id)
        board.state = new_state
        game = Sudoku()
        game.board = new_state
        new_status = game.sudoku_status()
        if new_status == 100.0:
            if json.dumps(new_state) != board.answer:
                new_status = 95.0
        board.isFinished = new_status
        board.save()
        return Response({"message": "Game saved successfully"})
    except Boards.DoesNotExist:
        return Response({"message": "Board not found"}, status=404)
