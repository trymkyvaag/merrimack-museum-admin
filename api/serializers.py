from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework import serializers as rest_serializers
from api.models import *


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


class PrivsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Privs
        fields = ["privs"]


class UserTypeSerializer(serializers.ModelSerializer):
    priv = PrivsSerializer(read_only=True)

    class Meta:
        model = UserType
        fields = ["user_type", "priv"]


# Category table, pk auto generated
class UserSerializer(serializers.ModelSerializer):
    user_type = UserTypeSerializer(read_only=True)
    # priv = PrivsSerializer(read_only=True)

    class Meta:
        model = User
        fields = ["address", "user_type"]

    def create(self, validated_data):
        address = validated_data.get("address")
        # Check if the user already exists with the given email address
        existing_user = User.objects.filter(address=address).first()
        if not existing_user:
            # Get or create the UserType instance with a user_type of "3"
            user_type, created = UserType.objects.get_or_create(user_type="student")
            validated_data["user_type"] = user_type
            user = User.objects.create(**validated_data)
            return user
        else:
            return existing_user


# Create a new serializer for updating user information
class UpdateUserSerializer(serializers.ModelSerializer):
    user_type = UserTypeSerializer()

    class Meta:
        model = User
        fields = ["address", "user_type"]

    def create(self, validated_data):
        user_type_value = validated_data.get("user_type")["user_type"]

        user_type_instance = UserType.objects.filter(user_type=user_type_value).first()
        if not user_type_instance:
            raise rest_serializers.ValidationError(
                f"UserType with the specified user_type '{user_type_value}' does not exist."
            )

        user_type_pk = user_type_instance.pk

        address = validated_data.get("address")
        # Check if the user already exists with the given email address
        existing_user = User.objects.filter(address=address).first()
        if existing_user:
            existing_user.user_type_id = user_type_pk
            existing_user.save()
            return existing_user


# Artwork table, handles attributes and foreign keys
class AddArtworkSerializer(serializers.ModelSerializer):
    # Foreign keys, not used when creating
    # or updating model instances based on incoming data (write-only set to True)
    artist_name = serializers.CharField(write_only=True)
    donor_name = serializers.CharField(write_only=True, required=False)
    location = serializers.CharField(write_only=True)
    category = serializers.CharField(write_only=True)

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
        )

    def create(self, validated_data):
        # Extract artist_name, donor_name, location_name, and category_name from the validated data
        artist_name = validated_data.pop("artist_name")
        donor_name = validated_data.pop("donor_name", None)
        location_name = validated_data.pop("location")
        category_name = validated_data.pop("category")

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

        # Create an Artwork instance, associating it with the Artist, Donor, Location, and Category instances
        artwork_instance = Artwork.objects.create(
            artist=artist_instance,
            donor=donor_instance,
            location=location_instance,
            category=category_instance,
            **validated_data,  # Include the remaining validated data
        )

        return artwork_instance


class KeywordSerializer(serializers.Serializer):
    keyword = serializers.CharField(required=True)


class ArtworkSearchInputSerializer(serializers.Serializer):
    keyword = serializers.CharField()


# Artwork table return all fields
class ArtworkSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    donor = DonorSerializer()
    location = LocationSerializer()
    category = CategorySerializer()

    class Meta:
        model = Artwork
        # Fields to include when serializing or deserializing
        fields = "__all__"
