from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register(r'custom-users', CustomUserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'donors', DonorViewSet)
router.register(r'artists', ArtistViewSet)
router.register(r'artworks', ArtworkViewSet)
router.register(r'migration-requests', MigrationRequestViewSet)
router.register(r'artwork-images', ArtworkImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
