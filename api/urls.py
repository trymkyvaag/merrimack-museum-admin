from django.urls import path
from .views import CreateArtworkView, ArtworkSearchView

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
]
