from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Artist, Artwork, Donor, Images, Location, Category
from api.serializers import ArtworkSerializer

print("Running addition test")


class CreateArtworkViewTest(TestCase):

    def test_create_artwork(self):
        print("Setup is good")

        artist_instance = Artist.objects.create(artist_name="Sample Artist")
        donor_instance = Donor.objects.create(donor_name="Sample Donor")
        location_instance = Location.objects.create(location="Sample Location")
        category_instance = Category.objects.create(category="Sample Category")
        image_instance = Images.objects.create(idimages=1,
                                               image_path="www.forbes.com/advisor/wp-content/uploads/2023/07/top-20-small-dog-breeds.jpg")

        artwork_data2 = {
            'title': 'Sample Artwork',
            'date_created_month': 5,
            'date_created_year': '2023',
            'comments': 'This is a sample artwork',
            'width': '20.5',
            'height': '15.0',
            'artist_name': 'Sample Artist',
            'donor_name': 'Sample Donor',
            'location': 'Sample Location',
            'category': 'Sample Category',
            'image_path': image_instance.image_path,
        }
        print(f"artwork: {artist_instance.artist_name}")

        serializer = ArtworkSerializer(data=artwork_data2)
        print("serializer created")

        if serializer.is_valid():
            print("Serializer is valid")
            serializer.save()
        else:
            print(serializer.errors)
            self.fail("Serializer is not valid")

        print("serializers saved")
        artwork = Artwork.objects.create(
            title=serializer.validated_data['title'],
            date_created_month=serializer.validated_data['date_created_month'],
            date_created_year=serializer.validated_data['date_created_year'],
            comments=serializer.validated_data['comments'],
            width=serializer.validated_data['width'],
            height=serializer.validated_data['height'],
            artist=artist_instance,
            donor=donor_instance,
            location=location_instance,
            category=category_instance,
            image_path=image_instance
        )
        print("running tests")

        self.assertEqual(artwork.title, "Sample Artwork")
        self.assertEqual(artwork.date_created_month, 5)
        # # Add more assertions for other fields

        # Clean up after the test
        artwork.delete()
