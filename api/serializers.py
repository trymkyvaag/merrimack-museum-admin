from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework import serializers as rest_serializers
from api.models import *
import random


# Artist table, pk auto generated
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["artist_name"]


# Donor table, pk auto generated
class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = ["donor_name"]


# Location table, pk auto generated
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["location"]


# Category table, pk auto generated
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category"]


# Images table, pk auto generated
class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ["image_path"]


# UserType table, pk auto generated
class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ["user_type"]


# User table, pk auto generated
# Used for adding/checking users or just checking existing user privs
class UserSerializer(serializers.ModelSerializer):
    # Nesting user_type serializer (fk in User table)
    user_type = UserTypeSerializer(read_only=True)

    class Meta:
        model = User
        fields = ["address", "user_type"]

    # create method for users
    # validated_data: address: "string"
    def create(self, validated_data):
        # gets the value from the input
        address = validated_data.get("address")
        # Check if the user already exists with the given email address
        # bu searching in the User table
        existing_user = User.objects.filter(address=address).first()
        if not existing_user:
            # Get or create the UserType instance with a user_type of "3"
            user_type, created = UserType.objects.get_or_create(user_type="student")
            validated_data["user_type"] = user_type
            user = User.objects.create(**validated_data)
            return user
            # Get or create the UserType instance with a user_type of "3" for student access
            # This initilizes all new users as student
            user_type, created = UserType.objects.get_or_create(user_type="student")
            validated_data[
                "user_type"
            ] = user_type  # set the validated data input (previosly null as its read only)
            user = User.objects.create(**validated_data)  # create the user
            return user  # return response
        else:
            # user already exists, return their info
            return existing_user


# Create a serializer for editing EXISTING user information
class UpdateUserSerializer(serializers.ModelSerializer):
    # Nest the user_type in here
    user_type = UserTypeSerializer()

    class Meta:
        model = User
        fields = ["address", "user_type"]

    # Lookup existing users
    # validated_data: address: "string", user_type: "string"
    def create(self, validated_data):
        # grab the value from the user_type input, first user_type is table name and second is the column name
        user_type_value = validated_data.get("user_type")["user_type"]
        # grab the value from the validated data
        address = validated_data.get("address")
        # find where there's a match on the user_type input
        user_type_instance = UserType.objects.filter(user_type=user_type_value).first()
        # if no match
        if not user_type_instance:
            raise rest_serializers.ValidationError(
                f"UserType with the specified user_type '{user_type_value}' does not exist."
            )

        # get primary key of the usertype requested
        user_type_pk = user_type_instance.pk
        # Check if the user already exists with the given email address, and if they do
        # then update their fk user_type value with the new one
        existing_user = User.objects.filter(address=address).first()
        if existing_user:
            existing_user.user_type_id = user_type_pk
            existing_user.save()
            return existing_user


# Artwork table, handles local columns and foreign key columns
class AddArtworkSerializer(serializers.ModelSerializer):
    # Foreign keys, not used when creating
    # or updating model instances based on incoming data (write-only set to True)
    artist_name = serializers.CharField(write_only=True)
    donor_name = serializers.CharField(
        write_only=True, required=False
    )  # donor name is not required
    location = serializers.CharField(write_only=True)
    category = serializers.CharField(write_only=True)
    image_path = serializers.CharField(write_only=True)

    class Meta:
        model = Artwork
        # Fields to include when serializing or deserializing
        fields = (
            "title",
            "date_created_month",
            "date_created_year",
            "comments",
            "width",
            "height",
            "artist_name",
            "donor_name",
            "location",
            "category",
            "image_path",
        )

    def create(self, validated_data):
        # Extract artist_name, donor_name, location_name, and category_name from the validated data
        artist_name = validated_data.pop("artist_name")
        donor_name = validated_data.pop("donor_name", None)
        location_name = validated_data.pop("location")
        category_name = validated_data.pop("category")
        img_path_name = validated_data.pop("image_path")
        # Get or create an Artist instance based on artist_name
        artist_instance, created = Artist.objects.get_or_create(artist_name=artist_name)

        donor_instance = None
        # Check if donor_name exists
        if donor_name:
            # Get or create a Donor instance based on donor_name
            donor_instance, created = Donor.objects.get_or_create(donor_name=donor_name)

        # Get or create a Location instance based on location_name
        location_instance, created = Location.objects.get_or_create(
            location=location_name
        )

        # Get or create a Category instance based on category_name
        category_instance, created = Category.objects.get_or_create(
            category=category_name
        )

        image_path_instance, created = Images.objects.get_or_create(
            image_path=img_path_name
        )

        image_path_instance.save()

        # Create an Artwork instance, associating it with the Artist, Donor, Location, and Category instances
        artwork_instance = Artwork.objects.create(
            artist=artist_instance,
            donor=donor_instance,
            location=location_instance,
            category=category_instance,
            image_path=image_path_instance,
            **validated_data,  # Include the remaining validated data
        )

        return artwork_instance


class KeywordSerializer(serializers.Serializer):
    keyword = serializers.CharField(required=True)


class ArtworkSearchInputSerializer(serializers.Serializer):
    """
    A serializer for keyword search

    ...

    Attributes
    ----------
    keyword : str
        keywords retrieved from frontend

    """

    keyword = serializers.CharField()


# Artwork table return all fields
class ArtworkSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    donor = DonorSerializer()
    location = LocationSerializer()
    category = CategorySerializer()
    image_path = ImagesSerializer()

    class Meta:
        model = Artwork
        # Fields to include when serializing or deserializing
        fields = "__all__"


# Artwork table return all fields
class ArtworkSerializerStandard(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        # Fields to include when serializing or deserializing
        fields = "__all__"


# Serializer class that returns random artwork
# Use case: when gallery page is loaded intially or refreshed
class RandomArtworkSerializer(serializers.Serializer):
    # create field that accepts integers only
    num_artworks = serializers.IntegerField()


# Add move request, use case: FS requesting an artwork piece
class MoveRequestSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # nester serialzier, grabs fk relation

    class Meta:
        model = MoveRequest
        fields = "__all__"

    # create request
    # validated data: address: string, to_location: string, is_pending: int(boolean), is_approving: int(boolean), comments: string, artwork_id: Artwork object (id)
    def create(self, validated_data):
        # Extract user data from the validated data
        user_data = validated_data.pop("user", None)
        # Try to get an existing user based on the provided data
        user_instance = User.objects.filter(**user_data).first()

        # If the user doesn't exist or the type of request isn't recognized
        if not user_instance:
            raise rest_serializers.ValidationError(
                f"The specified values either do not exist or are unexpected."
            )

        # Create RequestType instance with the linked User instance
        request_type_instance = MoveRequest.objects.create(
            user=user_instance, **validated_data
        )

        return request_type_instance


# return move requests given a username, use case: loading request page for a FS account
class ReturnMoveRequestsSerializer(serializers.Serializer):
    address = serializers.CharField()

    def to_representation(self, instance):
        address = self.validated_data["address"]

        # Use double underscores to traverse the foreign key relationship
        queryset = MoveRequest.objects.filter(user__address__iexact=address).order_by(
            "-time_stamp"
        )

        # Take only the first result (latest timestamp)
        latest_move_request = queryset.first()

        # Now you can serialize the latest MoveRequest and return the data
        serialized_data = (
            MoveRequestSerializer2(latest_move_request).data
            if latest_move_request
            else None
        )
        return {"move_request": serialized_data}


class MoveRequestSerializer2(serializers.ModelSerializer):
    user = UserSerializer()  # nester serialzier, grabs fk relation
    artwork = ArtworkSerializer()

    class Meta:
        model = MoveRequest
        fields = "__all__"
