from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.utils import timezone
from api.models import CustomUser, Category, Location, Donor, Artist, Artwork, MigrationRequest, ArtworkImage

class Command(BaseCommand):
    help = 'Populate custom models with sample data'

    def handle(self, *args, **options):
        self.populate_custom_users()
        self.populate_categories()
        self.populate_locations()
        self.populate_donors()
        self.populate_artists()
        self.populate_artworks()
        self.populate_migration_requests()
        self.populate_artwork_images()

        self.stdout.write(self.style.SUCCESS('Data populated successfully'))

    def populate_custom_users(self):
        # Check if the user already exists before creating
        if not CustomUser.objects.filter(username='faculty_user').exists():
            CustomUser.objects.create(username='faculty_user', is_faculty=True)

        if not CustomUser.objects.filter(username='student_user').exists():
            CustomUser.objects.create(username='student_user', is_student=True)

        if not CustomUser.objects.filter(username='admin_user').exists():
            CustomUser.objects.create(username='admin_user', is_admin=True)

    def populate_categories(self):
        # Check if the category already exists before creating
        if not Category.objects.filter(category_name='Category1').exists():
            Category.objects.create(category_name='Category1', description='Description for Category1')

        if not Category.objects.filter(category_name='Category2').exists():
            Category.objects.create(category_name='Category2', description='Description for Category2')

    def populate_locations(self):
        # Check if the location already exists before creating
        if not Location.objects.filter(location_name='Location1').exists():
            Location.objects.create(location_name='Location1', address='Address1', city='City1', state='State1', country='Country1')

        if not Location.objects.filter(location_name='Location2').exists():
            Location.objects.create(location_name='Location2', address='Address2', city='City2', state='State2', country='Country2')

    def populate_donors(self):
        # Check if the donor already exists before creating
        if not Donor.objects.filter(donor_name='Donor1').exists():
            Donor.objects.create(donor_name='Donor1', contact_email='donor1@example.com', donation_date=timezone.now())

        if not Donor.objects.filter(donor_name='Donor2').exists():
            Donor.objects.create(donor_name='Donor2', contact_email='donor2@example.com', donation_date=timezone.now())

    def populate_artists(self):
        # Check if the artist already exists before creating
        if not Artist.objects.filter(artist_name='Artist1').exists():
            Artist.objects.create(artist_name='Artist1', birth_date=timezone.now(), nationality='Nationality1', bio='Bio for Artist1')

        if not Artist.objects.filter(artist_name='Artist2').exists():
            Artist.objects.create(artist_name='Artist2', birth_date=timezone.now(), nationality='Nationality2', bio='Bio for Artist2')

    def populate_artworks(self):
        # Check if the artwork already exists before creating
        if not Artwork.objects.filter(title='Artwork1').exists():
            artist1 = Artist.objects.get(artist_name='Artist1')
            category1 = Category.objects.get(category_name='Category1')
            location1 = Location.objects.get(location_name='Location1')
            donor1 = Donor.objects.get(donor_name='Donor1')

            Artwork.objects.create(artist=artist1, title='Artwork1', creation_date=timezone.now(), description='Description for Artwork1',
                                   category=category1, location=location1, donor=donor1)

    def populate_migration_requests(self):
        # Check if the migration request already exists before creating
        if not MigrationRequest.objects.filter(status='Pending').exists():
            artwork1 = Artwork.objects.get(title='Artwork1')
            location1 = Location.objects.get(location_name='Location1')
            location2 = Location.objects.get(location_name='Location2')
            user = CustomUser.objects.get(username='admin_user')

            MigrationRequest.objects.create(user=user, artwork=artwork1, request_date=timezone.now(), current_location=location1,
                                            new_location=location2, status='Pending')

    def populate_artwork_images(self):
        # Check if the artwork image already exists before creating
        if not ArtworkImage.objects.filter(description='Description for Image1').exists():
            artwork1 = Artwork.objects.get(title='Artwork1')
            ArtworkImage.objects.create(artwork=artwork1, image_file='https://example.com/image1.jpg', description='Description for Image1')
