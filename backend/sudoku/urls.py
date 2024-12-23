from django.urls import path
from . import views

"""
    This is a list of URLs that the Django framework uses for the API.
    Each of these URL links are used by the React frontend to send data
    to the database.

    URLs
        "": generic index page that isn't used by frontend
        signin: the page that handles the sign in request
        signup: the page that handles the sign up request
        board: the page that handles creating a new board
        save: the page that handles saving a board
        saved-game: the page that handles gathering the boards of a user
"""


urlpatterns = [
    path("", views.index, name="index"),
    path("signin/", views.signin_view, name="signin"),
    path("signup/", views.signup_view, name="signup"),
    path("board/", views.get_game_by_difficulty, name="board"),
    path("save/", views.save_game_state, name="save"),
    path("saved-game/", views.load_saved_game, name="saved-game"),
]
