from django.shortcuts import render, redirect, get_object_or_404

# Django's built-in User model
from django.contrib.auth.models import User

# To convert a normal Django function into an API view.
from rest_framework.decorators import api_view

# To send data back to the frontend in JSON format.
from rest_framework.response import Response

# To specify HTTP status codes in API responses.
from rest_framework import status

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


# Create your views here.
@api_view(["POST"])
def register(request):
    # Gets only the username value.
    username = request.data["username"]
    email = request.data.get("email")
    password = request.data.get("password")

    user = User.objects.create_user(username=username, email=email, password=password)

    return Response(
        {"message": "User registartion successfully...!"},
        status=status.HTTP_201_CREATED,
    )


@api_view(["POST"])
def user_login(request):

    # Get username and password
    username = request.data.get("username")
    password = request.data.get("password")

    # Check username and password
    user = authenticate(username=username, password=password)

    if user:
        # Generate or get existing token
        token, create = Token.objects.get_or_create(user=user)
        # token.key	: Gets the actual token value
        return Response({"message": "Login successful", "token": token.key})

    else:
        return Response({"message": "Invalid username or password"}, status=401)

# Postman sent username and password.
# Django checked the credentials using authenticate().
# Credentials were correct.
# Django generated or retrieved the user's token.
# Django returned the token to Postman.
