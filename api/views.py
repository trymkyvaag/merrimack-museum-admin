from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


# Create your views here.


# Responsible for adding an artwork to the database
# Use case: Admin -> ADD
class AddArtwork(APIView):
    serializer_class = ArtworkSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()  # This will call the custom create() method in ArtworkSerializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Responsible for storing a new user to the db or retrieving a current user's info
# Use case: Login -> set header tabs and session variables correctly
class AddOrCheckUser(APIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            address = serializer.validated_data["address"]

            # Check if a user with the given address already exists
            existing_user = User.objects.filter(address=address).first()

            if existing_user:
                # If the user exists, return the existing user's information
                return Response(
                    UserSerializer(existing_user).data, status=status.HTTP_200_OK
                )
            else:
                # If the user doesn't exist, create a new user
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Responsible for returning a valid user
# Use case: Checking that user selected from list does in fact exist in the db, else return error
class CurrentUserPrivs(APIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            address = serializer.validated_data["address"]

            # Verify the given address exists
            existing_user = User.objects.filter(address=address).first()

            if existing_user:
                # If the user verifies, return the existing user's current information
                return Response(
                    UserSerializer(existing_user).data, status=status.HTTP_200_OK
                )
            # Bad, request trying to elevate privs of a user that does not exist
            else:
                error_message = {"error": "User with the given address does not exist."}
                return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUser(APIView):
    serializer_class = UpdateUserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"message": "User updated/created successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditArtworkView(APIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
