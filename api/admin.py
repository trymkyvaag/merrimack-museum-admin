from django.contrib import admin
from .models import CustomUser, Category, Location, Donor, Artist, Artwork, MigrationRequest, ArtworkImage

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_faculty', 'is_student', 'is_admin')
    list_filter = ('is_faculty', 'is_student', 'is_admin')
    search_fields = ('username',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'description')
    search_fields = ('category_name',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('location_name', 'address', 'city', 'state', 'country')
    search_fields = ('location_name', 'address', 'city', 'state', 'country')

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('donor_name', 'contact_email', 'donation_date')
    search_fields = ('donor_name', 'contact_email')

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('artist_name', 'birth_date', 'nationality', 'bio')
    search_fields = ('artist_name', 'nationality')

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist_name', 'creation_date', 'category_name', 'location_name', 'donor_name')

    def artist_name(self, obj):
        return obj.artist.artist_name

    def category_name(self, obj):
        return obj.category.category_name

    def location_name(self, obj):
        return obj.location.location_name

    def donor_name(self, obj):
        return obj.donor.donor_name

    artist_name.short_description = 'Artist'
    category_name.short_description = 'Category'
    location_name.short_description = 'Location'
    donor_name.short_description = 'Donor'

    search_fields = ('title', 'artist__artist_name', 'category__category_name', 'location__location_name', 'donor__donor_name')

@admin.register(MigrationRequest)
class MigrationRequestAdmin(admin.ModelAdmin):
    list_display = ('email', 'artwork', 'request_date', 'status')
    list_filter = ('status', 'request_date')
    search_fields = ('email', 'artwork__name') 

@admin.register(ArtworkImage)
class ArtworkImageAdmin(admin.ModelAdmin):
    list_display = ('artwork_name', 'image_file', 'description')
    search_fields = ('artwork__title', 'description')

    def artwork_name(self, obj):
        return obj.artwork.title
