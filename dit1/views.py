from django.shortcuts import render
from django.http import HttpResponse
from .models import Artist, Artwork


# Create your views here.


# This view will take name as a parmater, and return all data
def search_by_artist(request):
    matching_artists = Artist.objects.filter(artist_name__icontains="Kidd")

    artworks = Artwork.objects.filter(artist__in=matching_artists).prefetch_related(
        "location", "category"
    )
    return render(request, "artwork_list.html", {"artworks": artworks})
