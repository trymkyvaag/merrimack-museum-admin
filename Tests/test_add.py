from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Artwork


class CreateArtworkViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_artwork(self):
        # Create a dictionary representing the data you want to send in the POST request
        artwork_data = {
            "title": "Sample Artwork",
            "date_created_month": 10,
            "date_created_year": 2023,
            "comments": "A beautiful artwork",
            "width": 100,
            "height": 150,
            "artist_name": "Sample Artist",
            "donor_name": "Sample Donor",
            "location": "Sample Location",
            "category": "Sample Category",
        }

        # Send a POST request to your view
        response = self.client.post(
            'http://127.0.0.1:8000/api/addartwork/', artwork_data, format='json')

        # Check that the response status code is 201 (created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check that the data was not saved in the database
        # Ensure the count is still 0
        self.assertEqual(Artwork.objects.count(), 0)

    def tearDown(self):
        # Clean up any data that may have been created during the test
        # This is not strictly necessary for the transactional test case, but it's good practice
        Artwork.objects.all().delete()
