from rest_framework import serializers

from api.models import Artwork, Artist


class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = (
            "idartwork",
            "title",
            "date_created_month",
            "date_created_year",
            "comments",
            "width",
            "height",
            "artist",
            "donor",
            "location",
            "category",
            "image_path",
        )


class ArtistSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("idartist", "artist_name")
