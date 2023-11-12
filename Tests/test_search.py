from django.test import TestCase

from api.models import Artist, Artwork, Donor, Images, Location, Category
from api.serializers import ArtworkSerializer
from django.db.models import Q


class SearchArtworkViewTest(TestCase):
    """
    Test  class for searching artwork

    ...

    Attributes
    ----------
    _

    Methods
    -------
    setUp()
        Set up two artwork objects via valid serializers
    test_create_artwork()
        Uses the search view to test only return one artwork
    tearDown()
        Cleans up all objects  


    """

    def setUp(self):
        image_instance = Images.objects.create(idimages=1,
                                               image_path="www.forbes.com/advisor/wp-content/uploads/2023/07/top-20-small-dog-breeds.jpg")
        image_instance2 = Images.objects.create(idimages=2,
                                                image_path="https://www.forbes.com/advisor/wp-content/uploads/2023/07/pomeranian.jpg")

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
        artwork_data2 = {
            'title': 'Bampel Artwork',
            'date_created_month': 6,
            'date_created_year': '2013',
            'comments': 'This is a not  artwork',
            'width': '203.5',
            'height': '153.0',
            'artist_name': 'bample Artist',
            'donor_name': 'bample Donor',
            'location': 'bample Location',
            'category': 'bample Category',
            'image_path': image_instance2.image_path}

        # Create the first artwork with 'Sample' in the title
        serializer = ArtworkSerializer(data=artwork_data)
        if serializer.is_valid():
            serializer.save()
        else:
            self.fail("Serializer is not valid")

        # Create the second artwork without 'Sample' in the title
        serializer2 = ArtworkSerializer(data=artwork_data2)
        if serializer2.is_valid():
            serializer2.save()
        else:
            self.fail("Serializer2 is not valid")

    # AFTER MERGE MAKE THIS A FUNCTION IN VIEWS
    def test_create_artwork(self):
        print("Setup is good")
        keyword_list = ["Sample"]
        queryset = Artwork.objects.none()
        for kw in keyword_list:
            q_filter = (
                Q(title__icontains=kw)
                | Q(comments__icontains=kw)
                | Q(width__icontains=kw)
                | Q(height__icontains=kw)
                | Q(location__location__icontains=kw)
                | Q(donor__donor_name__icontains=kw)
                | Q(category__category__icontains=kw)
                # Add more fields here as needed
            )
            queryset |= Artwork.objects.filter(q_filter)

        results = ArtworkSerializer(queryset, many=True)
        # Assert search only gets one of the two artworks
        self.assertEquals(len(results.data), 1)

    def tearDown(self):
        # Clean up the test database
        print("Tear down")
        Artwork.objects.all().delete()
        Artist.objects.all().delete()
        Donor.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
        Images.objects.all().delete()
