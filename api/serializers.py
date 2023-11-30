from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework import serializers as rest_serializers
from api.models import *
import random

# ------------------------------------------------------------------------------------------------------------------
# STANDARD serializers for all tables in the database:


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


# Artwork table, pk auto generated, return all fields including values of
# foreign key id relations
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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["address"]


# UserType table, pk auto generated, return user_type
class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ["user_type"]


class MoveRequestSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    artwork = ArtworkSerializer()

    class Meta:
        model = MoveRequest
        fields = "__all__"


# ------------------------------------------------------------------------------------------------------------------
# Login Page Endpoints


# AddOrCheckUserSerializer -> GOAL: Given an (email) address,
# check whether they need to be added to the database as a new user or not.
# UTILIZES: A custom 'User' class, pk auto generated, nested user_type
# Use case:
#   1. On inital login, check if user is new or returning
#   2. After login, set header tabs correctly depending on user_type returned
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
            user_type, created = UserType.objects.get_or_create(user_type="Student")
            # Set new user's user_type as student
            validated_data["user_type"] = user_type
            # Save the all the data to the database and return info to client
            user = User.objects.create(**validated_data)
            return user
        else:
            # User already exists, return their info
            return existing_user


# ------------------------------------------------------------------------------------------------------------------
# Gallery Page Endpoints


# ArtworkSearchInputSerializer -> GOAL: Given a keyword as input,
# return artwork found
# UTILIZES: Artwork table
# Use case:
#   1. Using the search bar on the gallery page to search artwork by
#   its various types (artist_name, title, etc.)
class ArtworkSearchInputSerializer(serializers.ModelSerializer):
    keyword = serializers.CharField(required=False)  # type: string

    class Meta:
        model = Artwork
        fields = ["keyword"]


# ArtworkSearchInputSerializer -> GOAL: Given an integer as input,
# return a randomized selection in amount of the given integer
# UTILIZES: Artwork table
# Use case:
#   1. When user selects a specified integer from the dropdown, load page
#   with updated amount of random images
class RandomArtworkSerializerInt(serializers.ModelSerializer):
    # type: int
    num_artworks = serializers.IntegerField()

    class Meta:
        model = Artwork
        fields = ["num_artworks"]


# ArtworkSearchInputSerializer -> GOAL: Given a string as input,
# return a randomized selection of all the artwork
# UTILIZES: Artwork table
# Use case:
#   1. When gallery page is loaded and/or refreshed,
#   display random selection of images
#   2. When user selects "all" from the dropdown, load page
#   with updated amount of random images
class RandomArtworkSerializerAll(serializers.ModelSerializer):
    # type: string
    all_artworks = serializers.CharField()

    class Meta:
        model = Artwork
        fields = ["all_artworks"]


# ------------------------------------------------------------------------------------------------------------------
# Admin/FS Request Page Endpoints


# MoveRequestSubmitionSerializer -> GOAL: Given form data for
# an artwork move request as input, save request
# UTILIZES: Custom MoveRequest class, nested user serializer
# Use case:
#   1. FS/Admin wanting to move an artwork from one location to another
#   with a formal request
class MoveRequestSubmitionSerializer(serializers.ModelSerializer):
    address = UserSerializer()  # nester serialzier, grabs fk relation

    class Meta:
        model = MoveRequest
        fields = [
            "address",  # nested serializer value
            "artwork",
            "to_location",
            "is_pending",
            "is_approved",
            "is_complete",
            "comments",
            "time_stamp",
        ]

    # create request method
    # validated data: address: string, to_location: string, is_pending: int(boolean), is_approving: int(boolean), comments: string, artwork_id: Artwork object (id)
    def create(self, validated_data):
        # Extract user data from the validated data
        user_data = validated_data.pop("address", None)
        # Try to get an existing user based on the provided data
        user_instance = User.objects.filter(**user_data).first()

        # If the user doesn't exist or the type of request isn't recognized
        if not user_instance:
            raise rest_serializers.ValidationError(
                f"The specified value either does not exist or wasn'y unexpected."
            )

        # Create RequestType instance with the linked User instance
        request_type_instance = MoveRequest.objects.create(
            user=user_instance, **validated_data
        )

        return request_type_instance


# return move requests given a username, use case: loading request page for a FS account
class ReturnMoveRequestsSerializer(serializers.ModelSerializer):
    address = serializers.CharField()

    class Meta:
        model = MoveRequest
        fields = ["address"]

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
            MoveRequestSerializer(latest_move_request).data
            if latest_move_request
            else None
        )
        return {"move_request": serialized_data}


# ------------------------------------------------------------------------------------------------------------------
# Admin Dashboard Endpoints


# UpdateUserSerializer -> GOAL: Given an (email) address and user_type value,
# check if they exist. If they do, update the user's user_type value with the new one.
# UTILIZES: A custom 'User' class, pk auto generated, nested user_type
# Use case:
#   1. Admin needs to elevate or de-elevate a user's privilige
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
# Use case:
#   1. Admin needs to add a new artwork entry into the database
class AddArtworkSerializer(serializers.ModelSerializer):
    # Input fields the foreign keys in an artwork
    artist_name = serializers.CharField(
        write_only=True, required=False, allow_null=True
    )
    donor_name = serializers.CharField(
        write_only=True, required=False, allow_null=True
    )  # donor name is not required
    location = serializers.CharField(write_only=True, required=False, allow_null=True)
    category = serializers.CharField(write_only=True, required=False, allow_null=True)
    image_path = serializers.CharField(write_only=True, required=False)

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
            "size",
        )

    # create method for adding the artwork
    def create(self, validated_data):
        # Extract artist_name, donor_name, location_name, and category_name VALUES from the validated data
        artist_name = validated_data.pop("artist_name", None)
        donor_name = validated_data.pop("donor_name", None)
        location_name = validated_data.pop("location", None)
        category_name = validated_data.pop("category", None)
        img_path_name = validated_data.pop("image_path", None)

        # FOR EACH instance of the extracted values, get or create them in the corresponding
        # relational table

        # Get or create a new artist in table: Artist
        artist_instance, created = (
            Artist.objects.get_or_create(artist_name=artist_name)
            if artist_name
            else (None, False)
        )

        # Get or create a new donor in table: Donor
        donor_instance, created = (
            Donor.objects.get_or_create(donor_name=donor_name)
            if donor_name
            else (None, False)
        )

        # Get or create a new location in table: Location
        location_instance, created = (
            Location.objects.get_or_create(location=location_name)
            if location_name
            else (None, False)
        )

        # Get or create a new category in table: Category
        category_instance, created = (
            Category.objects.get_or_create(category=category_name)
            if category_name
            else (None, False)
        )

        # Get or create a new image_path in table: Images
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
            **validated_data,  # Include the remaining validated data aka the nonrelational fields like title and date_created_-
        )

        return artwork_instance  # return to view


class EditArtworkSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(required=False)
    donor = DonorSerializer(required=False)
    location = LocationSerializer(required=False)
    category = CategorySerializer(required=False)
    image_path = ImagesSerializer(required=False)

    class Meta:
        model = Artwork
        fields = "__all__"

    def update(self, instance, validated_data):
        artist_data = validated_data.pop("artist", None)
        donor_data = validated_data.pop("donor", None)
        location_data = validated_data.pop("location", None)
        category_data = validated_data.pop("category", None)
        image_path = validated_data.pop("image_path", None)

        instance = super().update(instance, validated_data)

        if artist_data:
            artist_instance, created = Artist.objects.get_or_create(**artist_data)
            instance.artist = artist_instance
        if donor_data:
            donor_instance, created = Donor.objects.get_or_create(**donor_data)
            instance.donor = donor_instance
        if location_data:
            location_instance, created = Location.objects.get_or_create(**location_data)
            instance.location = location_instance
        if category_data:
            category_instance, created = Category.objects.get_or_create(**category_data)
            instance.category = category_instance
        if image_path:
            image_path_instance, created = Images.objects.get_or_create(**image_path)
            instance.image_path = image_path_instance

        # Update the fields of the instance manually
        instance.title = validated_data.get("title", instance.title)
        instance.date_created_month = validated_data.get(
            "date_created_month", instance.date_created_month
        )
        instance.date_created_year = validated_data.get(
            "date_created_year", instance.date_created_year
        )
        instance.donor = validated_data.get("donor", instance.donor)
        instance.artist = validated_data.get("artist", instance.artist)
        instance.comments = validated_data.get("comments", instance.comments)
        instance.width = validated_data.get("width", instance.width)
        instance.height = validated_data.get("height", instance.height)
        instance.size = validated_data.get("size", instance.size)

        instance.save()
        return instance

    def delete(self, instance):
        # Delete the instance
        instance.delete()


class MoveRequestUpdateSerializer(serializers.ModelSerializer):
    type = serializers.CharField(write_only=True)

    class Meta:
        model = MoveRequest
        fields = ["type"]
