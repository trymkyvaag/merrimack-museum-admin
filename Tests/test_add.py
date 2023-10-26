from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Artwork
from api.serializers import ArtworkSerializer
from api.views import CreateArtworkView


class CreateArtworkViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_artwork(self):
        data = {
            "title": "Test add",
            "date_created_month": 1,
            "date_created_year": 2023,
            "comments": "Test comments",
            "width": 100,
            "height": 200,
            "artist_name": "Test Name",
            "location": "Test Name",
            "category": "Test Name",
        }

        response = self.client.post(
            '/api/create-artwork/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Artwork.objects.count(), 1)
        artwork = Artwork.objects.first()
        self.assertEqual(artwork.title, "Test add")

        serializer = ArtworkSerializer(artwork)
        self.assertEqual(response.data, serializer.data)
