from django.urls import path
from . import views

urlpatterns = [
    path("", views.search_by_artist, name="search_by_artist"),
]
