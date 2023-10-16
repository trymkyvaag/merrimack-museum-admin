from django.urls import path
from .views import CreateArtworkView

urlpatterns = [
    path(
        # end-point for adding new artwork to db
        "addartwork/",
        CreateArtworkView.as_view(),
    ),
    # path("create-artist", CreateArtistView.as_view()),
]
