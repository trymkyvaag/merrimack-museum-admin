from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework import serializers as rest_serializers
from api.models import *
import random

# ------------------------------------------------------------------------------------------------------------------
# Standard serializers for the following tables in the database:


# Artwork table, pk auto generated, return all fields
class ArtworkSerializerStandard(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        # Fields to include when serializing or deserializing
        fields = "__all__"


# Artist table, pk auto generated, return artist_name
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["artist_name"]


# Donor table, pk auto generated, return donor_name
class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = ["donor_name"]


# Location table, pk auto generated, return location
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["location"]


# Category table, pk auto generated, return category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category"]


# Images table, pk auto generated, return image_path
class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ["image_path"]


# UserType table, pk auto generated, return user_type
class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ["user_type"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["address"]


# ------------------------------------------------------------------------------------------------------------------
# Serializers for specific end point tasks


# AddOrCheckUserSerializer -> GOAL: Given an (email) address,
# check whether they need to be added to the database as a new user or not.
# UTILIZES: A custom 'User' class, pk auto generated, nested user_type
class AddOrCheckUserSerializer(serializers.ModelSerializer):
    # Nested user_type, gives actual value instead of the foreign key id
    # Set to read only because it is not used as input, only output
    user_type = UserTypeSerializer(read_only=True)

    # Custom User class with specified fields required
    class Meta:
        model = User
        fields = ["address", "user_type"]

    # create method for users
    # validated_data: address: "string"
    def create(self, validated_data):
        # gets the value from the inputed string address
        address = validated_data.get("address")
        # Check if the user already exists with the given email address
        # by searching in the User table
        existing_user = User.objects.filter(address=address).first()
        # If the user doesn't exist, create a new user
        if not existing_user:
            # Get or create the UserType instance with a user_type of "student"
            user_type, created = UserType.objects.get_or_create(user_type="student")
            # Set new user's user_type as student
            validated_data["user_type"] = user_type
            # Save the all the data to the database and return info to client
            user = User.objects.create(**validated_data)
            return user
        else:
            # User already exists, return their info
            return existing_user


# UpdateUserSerializer -> GOAL: Given an (email) address and user_type value,
# check if they exist. If they do, update the user's user_type value with the new one.
# UTILIZES: A custom 'User' class, pk auto generated, nested user_type
class UpdateUserSerializer(serializers.ModelSerializer):
    # Nested user_type, gives actual value instead of the foreign key id
    # Set to read only because it is not used as input, only output
    user_type = UserTypeSerializer()

    # Custom User class with specified fields required
    class Meta:
        model = User
        fields = ["address", "user_type"]

    # Lookup existing users and 'create' their new information
    # validated_data: address: "string", user_type: "string"
    def create(self, validated_data):
        # grab the user_type value, first user_type is table name and second is the column name
        user_type_value = validated_data.get("user_type")["user_type"]
        # grab the address value
        address = validated_data.get("address")
        # find where there's a match on the user_type input
        user_type_instance = UserType.objects.filter(user_type=user_type_value).first()
        # if no match is found
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


# AddArtworkSerializer -> GOAL: Given the artwork data fields,
# add a new artwork to the database. Must update relational tables.
# UTILIZES: A custom 'Artwork' class, pk auto generated
class AddArtworkSerializer(serializers.ModelSerializer):
    # Input fields the foreign keys in an artwork
    artist_name = serializers.CharField(write_only=True)
    donor_name = serializers.CharField(
        write_only=True, required=False
    )  # donor name is not required
    location = serializers.CharField(write_only=True)
    category = serializers.CharField(write_only=True)
    image_path = serializers.CharField(write_only=True)

    # custom class using the artwork model
    class Meta:
        model = Artwork
        # Fields to include when serializing or deserializing, note the artist_name ... image_path are the
        # input fields. On submission, must update the relational tables with these values then store the appropiate
        # foreign key id's in the artwork table.
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

    # create method for adding the artwork
    def create(self, validated_data):
        # Extract artist_name, donor_name, location_name, and category_name VALUES from the validated data
        artist_name = validated_data.pop("artist_name")
        donor_name = validated_data.pop("donor_name", None)
        location_name = validated_data.pop("location")
        category_name = validated_data.pop("category")
        img_path_name = validated_data.pop("image_path")

        # FOR EACH instance of the extracted values, get or create them in the corresponding
        # relational table

        # Get or create a new artist in table: Artist
        artist_instance, created = Artist.objects.get_or_create(artist_name=artist_name)

        donor_instance = None
        # Check if donor_name exists
        if donor_name:
            # Get or create a new donor in table: Donor
            donor_instance, created = Donor.objects.get_or_create(donor_name=donor_name)

        # Get or create a new location in table Location
        location_instance, created = Location.objects.get_or_create(
            location=location_name
        )

        # Get or create a new category in table: Category
        category_instance, created = Category.objects.get_or_create(
            category=category_name
        )
        # Get or create a new image_path in table: Images
        image_path_instance, created = Images.objects.get_or_create(
            image_path=img_path_name
        )

        image_path_instance.save()  # not sure why I need to save this but it's breaking if I don't

        # Create an Artwork instance, associating it with the Artist, Donor, Location, and Category instances
        artwork_instance = Artwork.objects.create(
            artist=artist_instance,
            donor=donor_instance,
            location=location_instance,
            category=category_instance,
            image_path=image_path_instance,
            **validated_data,  # Include the remaining validated data aka the nonrelational fields like title and date_created_-
        )

        return artwork_instance  # return to view


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
