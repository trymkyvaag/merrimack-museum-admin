from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'is_admin', 'is_faculty', 'is_student')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'description')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'location_name', 'address', 'city', 'state', 'country')

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = ('id', 'donor_name', 'contact_email', 'donation_date')

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'artist_name', 'birth_date', 'nationality', 'bio')

class ArtworkSerializer(serializers.ModelSerializer):
    artist_id = serializers.IntegerField(source='artist.id')
    artist_name = serializers.CharField(source='artist.artist_name')
    artist_birth_date = serializers.DateField(source='artist.birth_date')
    artist_nationality = serializers.CharField(source='artist.nationality')
    artist_bio = serializers.CharField(source='artist.bio')

    category_id = serializers.IntegerField(source='category.id')
    category_name = serializers.CharField(source='category.category_name')
    category_description = serializers.CharField(source='category.description')

    location_id = serializers.IntegerField(source='location.id')
    location_name = serializers.CharField(source='location.location_name')
    location_address = serializers.CharField(source='location.address')
    location_city = serializers.CharField(source='location.city')
    location_state = serializers.CharField(source='location.state')
    location_country = serializers.CharField(source='location.country')

    donor_id = serializers.IntegerField(source='donor.id')
    donor_name = serializers.CharField(source='donor.donor_name')
    donor_contact_email = serializers.EmailField(source='donor.contact_email')
    donor_donation_date = serializers.DateField(source='donor.donation_date')

    class Meta:
        model = Artwork
        fields = ('id', 'artist_id', 'artist_name', 'artist_birth_date', 'artist_nationality', 'artist_bio',
                  'title', 'creation_date', 'description',
                  'category_id', 'category_name', 'category_description',
                  'location_id', 'location_name', 'location_address', 'location_city', 'location_state', 'location_country',
                  'donor_id', 'donor_name', 'donor_contact_email', 'donor_donation_date')

class MigrationRequestSerializer(serializers.ModelSerializer):
    artwork_id = serializers.IntegerField(source='artwork.id')
    artwork_title = serializers.CharField(source='artwork.title')
    artwork_creation_date = serializers.DateField(source='artwork.creation_date')
    artwork_description = serializers.CharField(source='artwork.description')

    current_location_id = serializers.IntegerField(source='current_location.id')
    current_location_name = serializers.CharField(source='current_location.location_name')
    current_location_address = serializers.CharField(source='current_location.address')
    current_location_city = serializers.CharField(source='current_location.city')
    current_location_state = serializers.CharField(source='current_location.state')
    current_location_country = serializers.CharField(source='current_location.country')

    # new_location_id = serializers.IntegerField(source='new_location.id')
    new_location_name = serializers.CharField(source='new_location.location_name')
    new_location_address = serializers.CharField(source='new_location.address')
    new_location_city = serializers.CharField(source='new_location.city')
    new_location_state = serializers.CharField(source='new_location.state')
    new_location_country = serializers.CharField(source='new_location.country')

    email = serializers.EmailField(required=False)

    class Meta:
        model = MigrationRequest
        fields = ('id', 'email', 'artwork_id', 'artwork_title', 'artwork_creation_date', 'artwork_description',
                  'request_date', 'current_location_id', 'current_location_name', 'current_location_address',
                  'current_location_city', 'current_location_state', 'current_location_country',
                  'new_location_name', 'new_location_address',
                  'new_location_city', 'new_location_state', 'new_location_country', 'status')

    def create(self, validated_data):
        # Extract nested data
        artwork_data = validated_data.pop('artwork', {})
        current_location_data = validated_data.pop('current_location', {})
        new_location_data = validated_data.pop('new_location', {})
        
        # Extract email from validated_data
        email = validated_data.pop('email', None)

        # Create or retrieve related objects
        artwork_instance, _ = Artwork.objects.get_or_create(**artwork_data)
        current_location_instance, _ = Location.objects.get_or_create(**current_location_data)
        new_location_instance, _ = Location.objects.get_or_create(**new_location_data)

        # Create the MigrationRequest object with the user
        migration_request = MigrationRequest.objects.create(
            email=email,
            artwork=artwork_instance,
            current_location=current_location_instance,
            new_location=new_location_instance,
            **validated_data
        )

        return migration_request
    
class ArtworkImageSerializer(serializers.ModelSerializer):
    artwork_data = ArtworkSerializer(source='artwork', read_only=True)
    class Meta:
        model = ArtworkImage
        fields = ('id', 'artwork_data', 'image_file', 'description')
