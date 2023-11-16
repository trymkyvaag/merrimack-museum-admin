from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.db.models import Q
from random import shuffle

# Create your views here.


# ------------------------------------------------------------------------------------------------------------------
# Standard db table views
# Uses ArtworkSerializer data
class ArtworksList(APIView):
    serializer_class = ArtworkSerializer

    # 'get' request type
    def get(self, format=None):
        # Query all objects from the Artwork table
        artworks = Artwork.objects.all()

        # Serialize the queryset
        serializer = self.serializer_class(artworks, many=True)

        # Return serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)


# ------------------------------------------------------------------------------------------------------------------
# Login Page Views
# Uses: AddOrCheckUserSerializer data
class AddOrCheckUser(APIView):
    serializer_class = AddOrCheckUserSerializer

    # 'post' request type
    def post(self, request, format=None):
        # grab data from serializer
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # get (email) address value
            address = serializer.validated_data["address"]

            # Check if a user with the given address already exists
            existing_user = User.objects.filter(address=address).first()

            if existing_user:
                # If the user exists, return the existing user's information
                return Response(
                    AddOrCheckUserSerializer(existing_user).data,
                    status=status.HTTP_200_OK,
                )
            else:
                # If the user doesn't exist, save new user and return info
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return BAD request if invalid serializer
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Uses: AddOrCheckUserSerializer data
class CurrentUserPrivs(APIView):
    serializer_class = AddOrCheckUserSerializer

    # 'post' request type
    def post(self, request, format=None):
        # grab data from serializer
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            address = serializer.validated_data["address"]

            # Verify the given address exists
            existing_user = User.objects.filter(address=address).first()

            if existing_user:
                # If the user verifies, return the existing user's current information
                return Response(
                    AddOrCheckUserSerializer(existing_user).data,
                    status=status.HTTP_200_OK,
                )
            # Bad, request trying to elevate privs of a user that does not exist
            else:
                error_message = {"error": "User with the given address does not exist."}
                # return BAD request if invalid serializer
                return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
        # return BAD request if invalid serializer
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ------------------------------------------------------------------------------------------------------------------
# Gallery Page Endpoints


# Uses ArtworkSearchInputSerializer and ArtworkSerializer data
class ArtworkSearchView(APIView):
    serializer_class = ArtworkSearchInputSerializer

    def post(self, request, format=None):
        keywords = request.data.get("keyword")
        # place all keywords in a list
        keyword_list = keywords.split() if keywords else []
        queryset = Artwork.objects.none()
        # filter for each keyword
        for kw in keyword_list:
            q_filter = (
                Q(title__icontains=kw)
                | Q(comments__icontains=kw)
                | Q(width__icontains=kw)
                | Q(height__icontains=kw)
                | Q(location__location__icontains=kw)
                | Q(donor__donor_name__icontains=kw)
                | Q(category__category__icontains=kw)
                | Q(artist__artist_name__icontains=kw)
                | Q(title__icontains=kw)
                | Q(date_created_year__icontains=kw)
                # Add more fields here as needed
            )
            queryset |= Artwork.objects.filter(q_filter)

        # return matching results
        results = ArtworkSerializer(queryset, many=True)
        return Response(results.data, status=status.HTTP_200_OK)


# Uses RandomArtworkSerializer and ArtworkSerializer
# Used for recieving integer inputs
class RandomArtworkViewInt(APIView):
    serializer_class = RandomArtworkSerializerInt

    def post(self, request, format=None):
        # grab data from serializer
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():  # if valid data
            # get number
            num_artworks = serializer.validated_data["num_artworks"]
            # get all artworks
            queryset = Artwork.objects.all()

            # if given number is larger than total db count
            if num_artworks > queryset.count():
                # set as total db count
                num_artworks = queryset.count()

            # get list of random artworks
            random_artworks = random.sample(list(queryset), num_artworks)
            artwork_serializer = ArtworkSerializer(random_artworks, many=True)
            # return data
            return Response(artwork_serializer.data, status=status.HTTP_200_OK)

        # return BAD request if invalid serializer
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Uses RandomArtworkSerializer and ArtworkSerializer
# Used for recieving string inputs
class RandomArtworkViewAll(APIView):
    serializer_class = RandomArtworkSerializerAll

    def post(self, request, format=None):
        # grab data from serializer
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():  # if valid data
            # get string
            all_artworks = serializer.validated_data["all_artworks"]
            if all_artworks.lower() == "all":
                # get all artworks
                queryset = Artwork.objects.all()
                queryset = list(queryset)  # Convert the queryset to a list
                shuffle(queryset)  # Shuffle the list to randomize the order
                artwork_serializer = ArtworkSerializer(queryset, many=True)
                # return data
                return Response(artwork_serializer.data, status=status.HTTP_200_OK)
            else:
                # Handle unexpected value error
                return Response(
                    {"message": "Unexpected value"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        # return BAD request if invalid serializer
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ------------------------------------------------------------------------------------------------------------------
# Admin/FS Request Page Endpoints


# Uses: MoveRequestSubmitionSerializer
class MoveRequest(APIView):
    serializer_class = MoveRequestSubmitionSerializer  # serializer data we're using

    # post request type
    def post(self, request, format=None):
        # grab data from serializer
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()  # save data
            return Response(
                {"message": "Request Type saved successfully"},
                status=status.HTTP_201_CREATED,
            )

        # return BAD request if invalid serializer
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Uses: ReturnMoveRequestsSerializer
class ReturnMoveRequest(APIView):
    serializer_class = ReturnMoveRequestsSerializer  # serializer data we're usin

    # post request type
    def post(self, request, format=None):
        # grab data from serializer
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ------------------------------------------------------------------------------------------------------------------
# Admin Dashboard Endpoints


# Uses: UpdateUserSerializer
class UpdateUser(APIView):
    serializer_class = UpdateUserSerializer

    # 'post' request type
    def post(self, request, format=None):
        # grab data from serializer
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()  # save the data
            return Response(
                {"message": "User updated successfully"},
                status=status.HTTP_201_CREATED,
            )
        # return BAD request if invalid serializer
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Uses AddArtworkSerializer data
class AddArtwork(APIView):
    serializer_class = AddArtworkSerializer

    # 'post' request type
    def post(self, request, format=None):
        # get data from serializer
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()  # Save data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return BAD request if invalid serializer
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
