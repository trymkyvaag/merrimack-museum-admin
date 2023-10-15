from django.contrib import admin
from django.urls import path
from .views import CreateArtworkView, CreateArtistView

urlpatterns = [
    path("create-artwork", CreateArtworkView.as_view()),
    path("create-artist", CreateArtistView.as_view()),

]
