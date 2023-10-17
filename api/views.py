from django.shortcuts import render

from api.models import Artwork
from .serializers import ArtworkSearchInputSerializer, ArtworkSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

# Create your views here.


# Responsible for adding an artwork to the database
# Use case: Admin -> ADD
class CreateArtworkView(APIView):
    serializer_class = ArtworkSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()  # This will call the custom create() method in ArtworkSerializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArtworkSearchView(APIView):
    def post(self, request):
        # IDK what to call this but for now just keyword
        keyword = request.data.get('keyword')
        print(f"Keyword recieved: {keyword}")
        if keyword:
            queryset = Artwork.objects.filter(
                Q(title__icontains=keyword) |
                Q(location__location__icontains=keyword) |
                Q(donor__donor_name__icontains=keyword) |
                Q(artist__artist_name__icontains=keyword)
                # Add more fields here as needed
            )
        else:
            # Return an empty queryset if no keyword is provided.
            queryset = Artwork.objects.none()

        results = ArtworkSerializer(queryset, many=True)

        return Response(results.data, status=status.HTTP_200_OK)
