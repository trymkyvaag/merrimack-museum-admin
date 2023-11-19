# your_app/tests/test_views.py
from rest_framework.test import APITestCase
from django.contrib.contenttypes.models import ContentType
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from api.models import *  # Import your models

class CustomUserViewSetTests(APITestCase):
    def setUp(self):
        self.group = Group.objects.create(name='Test Group')

        # Check if the content type already exists
        content_type, created = ContentType.objects.get_or_create(
            model='customuser',
            app_label='your_app'
        )

        if created:
            # Create a permission and associate it with the content type
            self.permission = Permission.objects.create(
                name='Test Permission',
                codename='test_permission',
                content_type=content_type
            )
        else:
            # Retrieve the existing permission associated with the content type
            self.permission = Permission.objects.get(
                name='Test Permission',
                codename='test_permission',
                content_type=content_type
            )

        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password',
            is_admin=True,
            is_faculty=True,
            is_student=True
        )
        self.user.groups.add(self.group)
        self.user.user_permissions.add(self.permission)

    def test_get_user_by_email(self):
        url = reverse('customuser-get-user-by-email')
        response = self.client.get(url, {'email': 'test@example.com'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'test@example.com')

    def test_get_user_by_email_missing_parameter(self):
        url = reverse('customuser-get-user-by-email')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class MigrationRequestViewSetTests(APITestCase):
    def test_list_migration_requests(self):
        url = reverse('migrationrequest-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_migration_requests_by_email(self):
        url = reverse('migrationrequest-list')
        response = self.client.get(url, {'email': 'test@example.com'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ArtworkImageViewSetTests(APITestCase):
    def test_retrieve_artwork_image(self):
        artwork_image = ArtworkImage.objects.create(image_file='path/to/image.jpg', description='Test Image')
        url = reverse('artworkimage-detail', args=[artwork_image.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('image_url', response.data)

# Add more tests as needed
