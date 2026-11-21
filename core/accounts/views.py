from django.shortcuts import render, redirect, get_object_or_404

# Django's built-in User model
from django.contrib.auth.models import User

# To convert a normal Django function into an API view.
from rest_framework.decorators import api_view

# To send data back to the frontend in JSON format.
from rest_framework.response import Response

# To specify HTTP status codes in API responses.
from rest_framework import status


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
