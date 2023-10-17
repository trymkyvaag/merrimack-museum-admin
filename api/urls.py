from django.urls import path
from .views import CreateArtworkView, ArtworkSearchView,  AddUserEmail

urlpatterns = [
    path(
        # end-point for adding new artwork to db
        "add-artwork/",
        CreateArtworkView.as_view(),
    ),

    path(
        # end-point for searching for artwork
        "searchartwork/",
        ArtworkSearchView.as_view(),

    ),
    path(
        # end-point for adding user to db
        "add-user/",
        AddUserEmail.as_view(),
    ),
]
