from rest_framework import serializers

from api.models import Artwork, Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["artist_name"]


class ArtworkSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(write_only=True)  # Nested serializer for artist

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
        )

    def create(self, validated_data):
        artist_name = validated_data.pop("artist_name")
        artist_instance, created = Artist.objects.get_or_create(artist_name=artist_name)
        artwork_instance = Artwork.objects.create(
            artist=artist_instance, **validated_data
        )
        return artwork_instance
