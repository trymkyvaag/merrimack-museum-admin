from django.contrib import admin
from django.urls import path
from .views import ArtistSearch

urlpatterns = [path("home", ArtistSearch.as_view())]
