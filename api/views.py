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


# Standard db table views
# Uses ArtworkSerializer data, filtered on data that is not pending in a move request
class ArtworksListFiltered(APIView):
    serializer_class = ArtworkSerializer

    def get(self, request, format=None):
        # Query artworks that do not have a corresponding move request with is_pending set to 1
        artworks = Artwork.objects.exclude(
            Q(moverequest__is_pending=1)
            | Q(moverequest__is_approved=1, moverequest__is_complete=0)
        )

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
        print("\n\n\n")
        print('in addorcheckSER:', request.data)
        print('request.data:', end=' ')
        print(request.data)

        if serializer.is_valid():
            print(f"Serializer data: {serializer.validated_data}")
            # get (email) address value
            print("\n\n\n")

            address = serializer.validated_data["address"] if len(
                serializer.validated_data.keys()) > 1 else None
            if address:
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
                error_message = {
                    "error": "User with the given address does not exist."}
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
        # print("\n\n\n")
        # print("In artworkserializer:")
        # print(f"data:{request.data}")
        keywords = request.data.get(
            "keyword") if request.data != 'All' else None
        # print(f"keywords:{request.data}")

        # print("\n\n\n")

        # place all keywords in a list
        keyword_list = keywords.split() if keywords else []
        print("keyword list: ", keyword_list)

        # if no keywords are given send everything
        if keyword_list == []:
            results = ArtworkSerializer(Artwork.objects.all(), many=True)
            return Response(results.data, status=status.HTTP_200_OK)
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
        if len(queryset) == 0:
            print("No match in database")
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
    #
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
class MoveRequestSave(APIView):
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
        print(serializer)
        if serializer.is_valid():
            serializer.save()  # Save data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return BAD request if invalid serializer
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Uses EditArtworkSerializer data
class EditArtwork(APIView):
    def put(self, request, pk):
        # Step 1: Retrieve the instance to be updated
        try:
            artwork = Artwork.objects.get(pk=pk)
        except Artwork.DoesNotExist:
            return Response(
                {"error": "Artwork not found"}, status=status.HTTP_404_NOT_FOUND
            )

        # Step 2: Instantiate the serializer with the existing instance and the updated data
        serializer = EditArtworkSerializer(artwork, data=request.data)

        # Step 3: Validate and save the serializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            artwork = Artwork.objects.get(pk=pk)
        except Artwork.DoesNotExist:
            return Response(
                {"error": "Artwork not found"}, status=status.HTTP_404_NOT_FOUND
            )
        artwork.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MigrationsList(APIView):
    serializer_class = MoveRequestSerializer

    # 'get' request type
    def get(self, request, format=None):
        # Filter MoveRequest objects where is_pending is equal to 1
        artworks = MoveRequest.objects.filter(
            Q(is_pending=1) & Q(is_complete=0))
        # Serialize the queryset
        serializer = self.serializer_class(artworks, many=True)

        # Return serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)


class MigrationsApprovedList(APIView):
    serializer_class = MoveRequestSerializer

    # 'get' request type
    def get(self, request, format=None):
        # Filter MoveRequest objects where is_pending is equal to 1
        artworks = MoveRequest.objects.filter(
            Q(is_pending=0) & Q(is_approved=1) & Q(is_complete=0)
        )
        # Serialize the queryset
        serializer = self.serializer_class(artworks, many=True)

        # Return serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)


class MigrationsUpdate(APIView):
    serializer_class = MoveRequestUpdateSerializer

    # 'put' request type for updating is_pending and is_approved
    def put(self, request, pk, format=None):
        try:
            # Retrieve the MoveRequest object with the given primary key (pk)
            artwork = MoveRequest.objects.get(pk=pk)

            # Update is_pending to 0
            artwork.is_pending = 0

            # Check the input string and update is_approved accordingly
            approval_status = request.data.get(
                "type"
            )  # Assuming the input string is passed in the request data
            if approval_status == "approve":
                artwork.is_approved = 1
            else:
                artwork.is_approved = 0

            # Save the updated object
            artwork.save()

            # Serialize the updated object
            serializer = self.serializer_class(artwork)

            # Return serialized data
            return Response(serializer.data, status=status.HTTP_200_OK)
        except MoveRequest.DoesNotExist:
            return Response(
                {"error": "MoveRequest not found"}, status=status.HTTP_404_NOT_FOUND
            )


class MigrationsCompleteUpdate(APIView):
    serializer_class = MoveRequestUpdateSerializer

    # 'put' request type for updating is_pending and is_approved
    def put(self, request, pk, format=None):
        try:
            # Retrieve the MoveRequest object with the given primary key (pk)
            artwork = MoveRequest.objects.get(pk=pk)

            # Update is_pending to 0

            # Check the input string and update is_approved accordingly
            approval_status = request.data.get(
                "type"
            )  # Assuming the input string is passed in the request data
            if approval_status == "complete":
                artwork.is_complete = 1
                artwork.is_pending = 0
            else:
                artwork.is_approved = 0
                artwork.is_pending = 1

            # Save the updated object
            artwork.save()

            # Retrieve the related Artwork object using pkArtwork
            pk_artwork = request.data.get("idArtwork")
            print(pk_artwork)
            artworkToUpdate = Artwork.objects.get(pk=pk_artwork)

            print(artworkToUpdate)
            # Create or retrieve the Location object based on the new_location string
            new_location_str = request.data.get("location")
            print(new_location_str)
            location, created = Location.objects.get_or_create(
                location=new_location_str
            )
            print(location)
            # Update the location field in the Artwork model
            artworkToUpdate.location = location
            artworkToUpdate.save()

            # Serialize the updated object
            serializer = self.serializer_class(artwork)

            # Return serialized data
            return Response(serializer.data, status=status.HTTP_200_OK)
        except MoveRequest.DoesNotExist:
            return Response(
                {"error": "MoveRequest not found"}, status=status.HTTP_404_NOT_FOUND
            )
