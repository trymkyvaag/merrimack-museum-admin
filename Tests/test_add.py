from django.test import TestCase

from api.models import Artist, Artwork, Donor, Images, Location, Category
from api.serializers import ArtworkSerializer

print("Running addition test")

#Test class
class CreateArtworkViewTest(TestCase):

    def test_create_artwork(self):
        print("Setup is good")

        artist_instance = Artist.objects.create(artist_name="Sample Artist")
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
        artwork = Artwork.objects.get(title='Sample Artwork')
        print("running tests")

        self.assertEqual(artwork.title, "Sample Artwork")
        self.assertEqual(artwork.date_created_month, 5)
        artworks_in_db = Artwork.objects.filter(title='Sample Artwork')
        print(artworks_in_db)
        self.assertEqual(artworks_in_db.count(), 1)
        
        artwork_from_db = artworks_in_db.first()
        self.assertEqual(artwork_from_db.title, 'Sample Artwork')
        self.assertEqual(artwork_from_db.date_created_month, 5)


        # Clean up after the test
        artwork.delete()



    def tearDown(self):
        # Clean up the test database
        print("Tear down")
        Artwork.objects.all().delete()
        Artist.objects.all().delete()
        Donor.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
        Images.objects.all().delete()
