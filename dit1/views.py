from django.shortcuts import render
from django.http import HttpResponse
from .models import Artist, Artwork


# Create your views here.


def artwork_list(request):
    artworks = Artwork.objects.filter(idartwork=180)
    return render(request, "artwork_list.html", {"artworks": artworks})


def search_by_artist(request):
    matching_artists = Artist.objects.filter(artist_name__icontains="Kevin")

    artist_ids = [artist.idartist for artist in matching_artists]

    artworks = Artwork.objects.filter(artist_id__in=artist_ids)
    
    return render(request, "artwork_list.html", {"artworks": artworks})
