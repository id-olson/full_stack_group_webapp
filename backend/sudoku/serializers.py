from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Users, Boards


class UsersSerializer(serializers.ModelSerializer):
    """
    Used to validate and save Users data.

    This class is used when transferring data from the frontent to the database.
    It takes in data, validates it, and then saves it using the Users model from
    models.py. In other words, this is the class that uses the models to connect to
    the database.

    Attributes:
        model: The class model that the serializer will use to connect to the corresponding table
        fields: the attributes of that class model which are also the columns of the corresponding
                table

    Methods:
        create(self, validated_data): Edited create method to encrypt password before entering it
                                      into the database
    """

    class Meta:
        model = Users
        fields = ["id", "pwd", "email"]

    def create(self, validated_data):
        validated_data["pwd"] = make_password(validated_data["pwd"])
        return super(UsersSerializer, self).create(validated_data)


class BoardSerializer(serializers.ModelSerializer):
    """
    Used to validate and save Boards data.

    This class is used when transferring data from the frontend to the database.
    It takes in data, validates it, and then saves it using the Boards model from
    models.py. In other words, this is the class that uses the models to connect to
    the database.

    Attributes:
        model: The class model that the serializer will use to connect to the corresponding table
        fields: the attributes of that class model which are also the columns of the corresponding
                table
    """

    class Meta:
        model = Boards
        fields = [
            "id",
            "state",
            "answer",
            "initial",
            "difficulty",
            "style",
            "user",
            "isFinished",
        ]
