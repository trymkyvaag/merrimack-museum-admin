from rest_framework import serializers

from api.models import Artwork, Artist, Donor, Location, Category


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


# Artwork table, handles attributes and foreign keys
class ArtworkSerializer(serializers.ModelSerializer):
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
        artist_instance, created = Artist.objects.get_or_create(
            artist_name=artist_name)

        donor_instance = None
        # Check if donor_name exists
        if donor_name:
            # Get or create a Donor instance based on donor_name
            donor_instance, created = Donor.objects.get_or_create(
                donor_name=donor_name)

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
            **validated_data  # Include the remaining validated data
        )

        return artwork_instance


# Artwork table, handles attributes and foreign keys
class ArtworkSearchSerializer(serializers.ModelSerializer):
    location = serializers.CharField(required=False)
    donor = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    artist = serializers.CharField(required=False)

    class Meta:
        fields = ('location', 'donor', 'name', 'artist')

    class Meta:
        model = Artwork
        # Fields to include when serializing or deserializing
        fields = (
            "title",
            "artist",
            "donor",
            "name",
            "location",
            "category",
        )

    def search(self, validated_data):
        # Extract artist_name, donor_name, location_name, and category_name from the validated data
        artist_name = validated_data.get("artist")
        donor_name = validated_data.get("donor")
        location_name = validated_data.get("location")
        category_name = validated_data.get("category")

        # Initialize variables for the instances
        artist_instance = None
        donor_instance = None
        location_instance = None
        category_instance = None

        # Get the Artist instance if artist_name is provided
        if artist_name:
            artist_instance = Artist.objects.filter(
                artist_name=artist_name).first()

        # Get the Donor instance if donor_name is provided
        if donor_name:
            donor_instance = Donor.objects.filter(
                donor_name=donor_name).first()

        # Get the Location instance if location_name is provided
        if location_name:
            location_instance = Location.objects.filter(
                location=location_name).first()

        # Get the Category instance if category_name is provided
        if category_name:
            category_instance = Category.objects.filter(
                category=category_name).first()

        # You can return these objects as a dictionary or a list, depending on your needs
        result = {
            "artist_instance": artist_instance,
            "donor_instance": donor_instance,
            "location_instance": location_instance,
            "category_instance": category_instance,
        }

        return result
