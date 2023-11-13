from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.db.models import Q

# Create your views here.


# Responsible for adding an artwork to the database
# Use case: Admin -> ADD
class AddArtwork(APIView):
    serializer_class = AddArtworkSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()  # This will call the custom create() method in AddArtworkSerializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArtworkSearchView(APIView):
    serializer_class = ArtworkSearchInputSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        keywords = request.data.get("keyword")
        keyword_list = keywords.split() if keywords else []
        queryset = Artwork.objects.none()
        for kw in keyword_list:
            q_filter = (
                Q(title__icontains=kw)
                | Q(comments__icontains=kw)
                | Q(width__icontains=kw)
                | Q(height__icontains=kw)
                | Q(location__location__icontains=kw)
                | Q(donor__donor_name__icontains=kw)
                | Q(category__category__icontains=kw)
                # Add more fields here as needed
            )
            queryset |= Artwork.objects.filter(q_filter)

        results = ArtworkSerializer(queryset, many=True)
        return Response(results.data, status=status.HTTP_200_OK)


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
            serializer.save()
            return Response(
                {"message": "User updated/created successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RandomArtworkView(APIView):
    serializer_class = RandomArtworkSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            num_artworks = serializer.validated_data["num_artworks"]
            queryset = Artwork.objects.all()

            if num_artworks > queryset.count():
                num_artworks = queryset.count()

            random_artworks = random.sample(list(queryset), num_artworks)
            artwork_serializer = ArtworkSerializer(random_artworks, many=True)
            return Response(artwork_serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MoveRequest(APIView):
    serializer_class = MoveRequestSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Request Type saved successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReturnMoveRequest(APIView):
    serializer_class = ReturnMoveRequestsSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
