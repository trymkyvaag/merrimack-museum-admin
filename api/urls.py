from django.urls import path
from .views import *

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
]
