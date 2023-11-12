from django.test import TestCase

from api.models import Artist, Artwork, Donor, Images, Location, Category
from api.serializers import ArtworkSerializer


class CreateArtworkViewTest(TestCase):
    """
    Test  class for adding an artwork

    ...

    Attributes
    ----------
    _

    Methods
    -------
    test_create_artwork()
        tests that addiing to the database is working as intended

    tearDown()
        cleans the test_dit1 (Testing db) 
    """

    def test_create_artwork(self):
        """
        Test adding to the test database and ensure the artwork object is correctly made

        Parameters
        ----------
        -
        """

        # Create image objects to correctly mock an artwork entry
        image_instance = Images.objects.create(idimages=1,
                                               image_path="www.forbes.com/advisor/wp-content/uploads/2023/07/top-20-small-dog-breeds.jpg")

        artwork_data = {
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

        # Using the serializer for adding to the mock db
        serializer = ArtworkSerializer(data=artwork_data)

        # Check serializer is created correctly and that all fields are valid
        if serializer.is_valid():
            print("Serializer is valid")
            serializer.save()
        else:
            print(serializer.errors)
            self.fail("Serializer is not valid")

        # Get the artwork from the db
        artwork = Artwork.objects.get(title='Sample Artwork')

        # Assert fields match types
        self.assertEqual(artwork.title, "Sample Artwork")
        self.assertEqual(artwork.date_created_month, 5)

        # Check we have one entry with given title added and that it is only one
        artworks_in_db = Artwork.objects.filter(title='Sample Artwork')
        self.assertEqual(artworks_in_db.count(), 1)

        # Another check that the first entry is the only entry and equal
        artwork_from_db = artworks_in_db.first()
        self.assertEqual(artwork_from_db.title, 'Sample Artwork')
        self.assertEqual(artwork_from_db.date_created_month, 5)

        # Delete the artwork
        artwork.delete()

    def tearDown(self):
        """
        Tear down all objects to clean up for next test

        Parameters
        ----------
        -
        """
        Artwork.objects.all().delete()
        Artist.objects.all().delete()
        Donor.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
        Images.objects.all().delete()
