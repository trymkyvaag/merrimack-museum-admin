from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.db import models
from api.storage_backends.PublicMediaStorage import PublicMediaStorage

class CustomUser(AbstractUser):
    is_faculty = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    # Set unique related_name arguments to avoid clashes
    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_user_permissions')

    # Add any additional fields or methods as needed

    def __str__(self):
        return self.username

class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Location(models.Model):
    location_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)

class Donor(models.Model):
    donor_name = models.CharField(max_length=255)
    contact_email = models.EmailField(null=True, blank=True)
    donation_date = models.DateField(null=True, blank=True)

class Artist(models.Model):
    artist_name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

class Artwork(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    creation_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    donor = models.ForeignKey(Donor, on_delete=models.SET_NULL, null=True)

class MigrationRequest(models.Model):
    email = models.EmailField(null=True, blank=True)
    artwork = models.ForeignKey(Artwork, on_delete=models.PROTECT)
    request_date = models.DateField()
    current_location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='current_location_requests', null=True)
    new_location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='new_location_requests', null=True)
    status = models.CharField(max_length=8, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied')])

class ArtworkImage(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, null=True, blank=True)
    image_file = models.FileField(storage=PublicMediaStorage(), upload_to='', default='uploads')
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
