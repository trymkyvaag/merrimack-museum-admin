# api/tests/test_models.py
from django.test import TestCase
from datetime import date
from api.models import (
    CustomUser,
    Category,
    Location,
    Donor,
    Artist,
    Artwork,
    MigrationRequest,
    ArtworkImage,
)

class CustomUserModelTest(TestCase):
    def test_custom_user_model(self):
        user = CustomUser.objects.create(username='testuser')
        self.assertEqual(user.username, 'testuser')
        self.assertFalse(user.is_faculty)
        self.assertFalse(user.is_student)
        self.assertFalse(user.is_admin)

class CategoryModelTest(TestCase):
    def test_category_model(self):
        category = Category.objects.create(category_name='Test Category', description='Test Description')
        self.assertEqual(category.category_name, 'Test Category')
        self.assertEqual(category.description, 'Test Description')

class LocationModelTest(TestCase):
    def test_location_model(self):
        location = Location.objects.create(
            location_name='Test Location',
            address='Test Address',
            city='Test City',
            state='Test State',
            country='Test Country',
        )
        self.assertEqual(location.location_name, 'Test Location')
        self.assertEqual(location.address, 'Test Address')
        self.assertEqual(location.city, 'Test City')
        self.assertEqual(location.state, 'Test State')
        self.assertEqual(location.country, 'Test Country')

class DonorModelTest(TestCase):
    def test_donor_model(self):
        donor = Donor.objects.create(donor_name='Test Donor', contact_email='test@example.com', donation_date=date(2022, 1, 1))
        self.assertEqual(donor.donor_name, 'Test Donor')
        self.assertEqual(donor.contact_email, 'test@example.com')
        self.assertEqual(donor.donation_date, date(2022, 1, 1))

class ArtistModelTest(TestCase):
    def test_artist_model(self):
        artist = Artist.objects.create(artist_name='Test Artist', birth_date=date(2000, 1, 1), nationality='Test Nationality', bio='Test Bio')
        self.assertEqual(artist.artist_name, 'Test Artist')
        self.assertEqual(artist.birth_date, date(2000, 1, 1))
        self.assertEqual(artist.nationality, 'Test Nationality')
        self.assertEqual(artist.bio, 'Test Bio')

class ArtworkModelTest(TestCase):
    def test_artwork_model(self):
        artist = Artist.objects.create(artist_name='Test Artist')
        category = Category.objects.create(category_name='Test Category')
        location = Location.objects.create(location_name='Test Location')
        donor = Donor.objects.create(donor_name='Test Donor')

        artwork = Artwork.objects.create(
            artist=artist,
            title='Test Artwork',
            creation_date=date(2022, 1, 1),
            description='Test Description',
            category=category,
            location=location,
            donor=donor,
        )

        self.assertEqual(artwork.artist.artist_name, 'Test Artist')
        self.assertEqual(artwork.title, 'Test Artwork')
        self.assertEqual(artwork.creation_date, date(2022, 1, 1))
        self.assertEqual(artwork.description, 'Test Description')
        self.assertEqual(artwork.category.category_name, 'Test Category')
        self.assertEqual(artwork.location.location_name, 'Test Location')
        self.assertEqual(artwork.donor.donor_name, 'Test Donor')

class MigrationRequestModelTest(TestCase):
    def test_migration_request_model(self):
        artwork = Artwork.objects.create(artist=Artist.objects.create(artist_name='Test Artist'), title='Test Artwork')
        location = Location.objects.create(location_name='Test Location')

        migration_request = MigrationRequest.objects.create(
            email='test@example.com',
            artwork=artwork,
            request_date=date(2022, 1, 1),
            current_location=location,
            new_location=location,
            status='Pending',
        )

        self.assertEqual(migration_request.email, 'test@example.com')
        self.assertEqual(migration_request.artwork, artwork)
        self.assertEqual(migration_request.request_date, date(2022, 1, 1))
        self.assertEqual(migration_request.current_location, location)
        self.assertEqual(migration_request.new_location, location)
        self.assertEqual(migration_request.status, 'Pending')

class ArtworkImageModelTest(TestCase):
    def test_artwork_image_model(self):
        artwork = Artwork.objects.create(artist=Artist.objects.create(artist_name='Test Artist'), title='Test Artwork')

        artwork_image = ArtworkImage.objects.create(
            artwork=artwork,
            image_file='test_image.jpg',
            description='Test Description',
        )

        self.assertEqual(artwork_image.artwork, artwork)
        self.assertEqual(artwork_image.image_file, 'test_image.jpg')
        self.assertEqual(artwork_image.description, 'Test Description')
