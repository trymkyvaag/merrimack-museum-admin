from django.shortcuts import render
from django.http import HttpResponse
from .models import Artist, Artwork


# Create your views here.


def artwork_list(request):
    artworks = Artwork.objects.all()
    return render(request, "artwork_list.html", {"artworks": artworks})
