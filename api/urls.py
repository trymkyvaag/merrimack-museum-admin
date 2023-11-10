from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'move-requests', MoveRequestViewSet, basename='move-request')

urlpatterns = [
    path(
        # end-point for adding new artwork to db
        "add-artwork/",
        AddArtwork.as_view(),
    ),
    path(
        # end-point for adding user to db
        "add-or-check-user/",
        AddOrCheckUser.as_view(),
    ),
    path(
        # end-point for adding user to db
        "current-user-privs/",
        CurrentUserPrivs.as_view(),
    ),
    path(
        # end-point for adding user to db
        "edit-user-privs/",
        UpdateUser.as_view(),
    ),
    path(
        # end-point for searching for artwork
        "searchartwork/",
        ArtworkSearchView.as_view(),
    ),
    path(
        # end-point for searching for artwork
        "randomartwork/",
        RandomArtworkView.as_view(),
    ),
    path('', include(router.urls)),
]
