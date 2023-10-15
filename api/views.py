from django.shortcuts import render
from .models import Artist, Artwork
from .serializers import ArtworkSerializer, ArtistSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class CreateArtistView(APIView):
    serializer_class = ArtistSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            artist_name = serializer.data.get("artist_name")

            artist = Artist(artist_name=artist_name)

            artist.save()

            return Response(
                ArtworkSerializer(artist).data, status=status.HTTP_201_CREATED
            )


# class CreateArtworkView(APIView):
#     serializer_class = ArtworkSerializer

#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)

#         if serializer.is_valid():
#             title = serializer.data.get("title")
#             date_created_month = serializer.data.get("date_created_month")
#             date_created_year = serializer.data.get("date_created_year")
#             comments = serializer.data.get("comments")
#             width = serializer.data.get("width")
#             height = serializer.data.get("height")

#             artwork = Artwork(
#                 title=title,
#                 date_created_month=date_created_month,
#                 date_created_year=date_created_year,
#                 comments=comments,
#                 width=width,
#                 height=height,
#             )

#             artwork.save()

#             return Response(
#                 ArtworkSerializer(artwork).data, status=status.HTTP_201_CREATED
#             )


class CreateArtworkView(APIView):
    serializer_class = ArtworkSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()  # This will call the custom create() method in ArtworkSerializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
