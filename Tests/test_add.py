from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Artwork
from api.serializers import ArtworkSerializer


class CreateArtworkViewTest(TestCase):

    def test_create_artwork(self):
        print("Setup is good")
        data = {
            "title": "My Artwork",
            "date_created_month": 10,
            "date_created_year": "2023",
            "comments": "This is a test artwork",
            "width": 10.5,
            "height": 15.2,
            "artist_name": "John Doe",  # Example artist name
            "donor_name": "Jane Smith",  # Example donor name
            "location": "Art Gallery",  # Example location
            "category": "Painting",  # Example category
        }
        print("data created")
        print("creating serializer")
        serializer = ArtworkSerializer(data=data)
        print("serializer created")

        if serializer.is_valid():
            print("Serializer is valid")
            serializer.save()
        else:
            self.fail("Serializer is not valid")

        print("serializers saved")

        # Add assertions to check if the object is created as expected
        artwork = Artwork.objects.get(title="My Artwork")
        print("running tests")

        self.assertEqual(artwork.title, "My Artwork")
        self.assertEqual(artwork.date_created_month, 10)
        # Add more assertions for other fields

        # Clean up after the test
        artwork.delete()


