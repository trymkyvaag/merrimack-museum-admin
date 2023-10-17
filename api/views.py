from django.shortcuts import render
from .serializers import ArtworkSerializer, ArtworkSearchSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Artwork
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
    def get(self, request):
        serializer = ArtworkSearchSerializer(data=request.query_params)
        if serializer.is_valid():
            location = serializer.validated_data.get('location', None)
            donor = serializer.validated_data.get('donor', None)
            name = serializer.validated_data.get('name', None)
            artist_name = serializer.validated_data.get('artist_name', None)

            # Perform the search
            queryset = Artwork.objects.all()

            if location:
                queryset = queryset.filter(
                    Q(location__location__icontains=location))

            if donor:
                queryset = queryset.filter(
                    Q(donor__donor_name__icontains=donor))

            if name:
                queryset = queryset.filter(Q(name__icontains=name))

            if artist_name:
                queryset = queryset.filter(
                    Q(artist__artist_name__icontains=artist_name))

            # Serialize the results
            results = ArtworkSerializer(queryset, many=True)
            return Response(results.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
