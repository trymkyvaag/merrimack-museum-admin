from rest_framework import serializers

from api.models import Artwork, Artist, Donor, Location, Category


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["artist_name"]


class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = ["donor_name"]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["location"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category"]


class ArtworkSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(write_only=True)  # Nested serializer for artist
    donor_name = serializers.CharField(write_only=True)
    location = serializers.CharField(write_only=True)
    category = serializers.CharField(write_only=True)

    class Meta:
        model = Artwork
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
        artist_name = validated_data.pop("artist_name")
        donor_name = validated_data.pop("donor_name")
        location_name = validated_data.pop("location")
        category_name = validated_data.pop("category")

        artist_instance, created = Artist.objects.get_or_create(artist_name=artist_name)
        donor_instance, created = Donor.objects.get_or_create(donor_name=donor_name)
        location_instance, created = Location.objects.get_or_create(
            location=location_name
        )
        category_instance, created = Category.objects.get_or_create(
            category=category_name
        )

        artwork_instance = Artwork.objects.create(
            artist=artist_instance,
            donor=donor_instance,
            location=location_instance,
            category=category_instance,
            **validated_data
        )

        return artwork_instance
