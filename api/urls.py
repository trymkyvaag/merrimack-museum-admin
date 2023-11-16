from django.urls import path
from .views import *

urlpatterns = [
    path(
        # end-point for adding new artwork to db
        "add-artwork/",
        AddArtwork.as_view(),
    ),
    path(
        # end-point for adding or checking user
        "add-or-check-user/",
        AddOrCheckUser.as_view(),
    ),
    path(
        # end-point for checking if user in db
        "current-user-privs/",
        CurrentUserPrivs.as_view(),
    ),
    path(
        # end-point for editing user control
        "edit-user-privs/",
        UpdateUser.as_view(),
    ),
    path(
        # end-point for searching for artwork
        "searchartwork/",
        ArtworkSearchView.as_view(),
    ),
    path(
        # end-point for returning random artwork
        "randomartwork/",
        RandomArtworkView.as_view(),
    ),
    path(
        # end-point for storing move request
        "move-request/",
        MoveRequest.as_view(),
    ),
    path(
        # end-point for returning the latest move request associated with a user
        "find-request/",
        ReturnMoveRequest.as_view(),
    ),
    path(
        # returns entire collection of artworks
        "artworks-list/",
        ArtworksList.as_view(),
    ),
]
