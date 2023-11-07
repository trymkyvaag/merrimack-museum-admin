from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Artist, Artwork, Donor, Images, Location, Category
from api.serializers import ArtworkSerializer


class CreateArtworkViewTest(TestCase):

    def test_create_artwork(self):
        print("Setup is good")

        artist_instance = Artist.objects.create(artist_name="Sample Artist")
        donor_instance = Donor.objects.create(donor_name="Sample Donor")
        location_instance = Location.objects.create(location="Sample Location")
        category_instance = Category.objects.create(category="Sample Category")
        image_instance = Images.objects.create(idimages=1,
                                               image_path="www.forbes.com/advisor/wp-content/uploads/2023/07/top-20-small-dog-breeds.jpg")

        # Artwork data with string values for location and category
        artwork_data = {
            'title': 'Sample Artwork',
            'date_created_month': 5,
            'date_created_year': '2023',
            'comments': 'This is a sample artwork',
            'width': '20.5',  # Converted to a string
            'height': '15.0',  # Converted to a string
            'artist': artist_instance.artist_name,  # Use the artist's name
            'donor': donor_instance.donor_name,  # Use the donor's name
            'location': location_instance.location,  # Use the location's name
            'category': category_instance.category,  # Use the category's name
            'image_path': image_instance.image_path,
        }

        serializer = ArtworkSerializer(data=artwork_data)
        print("serializer created")

        if serializer.is_valid():
            print("Serializer is valid")
            serializer.save()
        else:
            print(serializer.errors)
            self.fail("Serializer is not valid")

        print("serializers saved")

        # Add assertions to check if the object is created as expected
        # artwork = Artwork.objects.create(**data)  # get(title="My Artwork")
        print("running tests")

        # self.assertEqual(artwork.title, "My Artwork")
        # self.assertEqual(artwork.date_created_month, 10)
        # # Add more assertions for other fields

        # # Clean up after the test
        # artwork.delete()
