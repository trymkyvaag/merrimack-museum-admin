from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Artist, Artwork
from .serializers import ArtistSerialzer


# Create your views here.
def main(request):
    return HttpResponse("Hello World")


class ArtistSearch(generics.CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerialzer
