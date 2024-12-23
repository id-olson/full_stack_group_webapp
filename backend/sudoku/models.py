from django.db import models


class Users(models.Model):
    """
    Handles SQL queries to the Users table

    This is the Django model class that is used to connect to the Users
    table in our MySQL database. Because of this, attributes for this
    class match the columns in the table.

    Attributes:
        id: The username for a user, unique to one person thus the primary key
        pwd: The password for a user, used to give access to the user's account
        email: The user's email, used for authentication purposes

    For more information on how to use this to connect to the table, see the Django documentation.
    """

    id = models.CharField(primary_key=True, max_length=30)
    pwd = models.CharField(max_length=128)
    email = models.CharField(max_length=200)


class Boards(models.Model):
    """
    Handles SQL queries to the Boards table

    This is the Django model class that is used to connect to the Boards
    table in our MySQL database. Because of this, attributes for this
    class match the columns in the table.

    Attributes:
        id: The primary key and just a number that is unique for each board
        state: The current state of the sudoku board
        answer: The solution for the sudoku board
        initial: The inital state of the sudoku board
        difficulty: The difficulty of the board. Difficulty is defined as how filled
                    in the board was at the start
        style: The type of sudoku puzzle it is. Could be normal sudoku, killer sudoku, etc.
        user: The username of the user who is working on that board
        isFinished: A float that represents the percentage of completion of the sudoku board

    For more information on how to use this to connect to the table, see the Django documentation.
    """

    id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    initial = models.CharField(max_length=500, default="")
    difficulty = models.CharField(max_length=30)
    style = models.CharField(max_length=30)
    user = models.CharField(max_length=30)
    isFinished = models.FloatField(default=0.0)
