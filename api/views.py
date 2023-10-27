from django.shortcuts import render

from api.models import Artwork
from .serializers import ArtworkSearchInputSerializer, ArtworkSerializer, KeywordSerializer
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
    serializer_class = ArtworkSearchInputSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        # IDK what to call this but for now just keyword
        # search_json = {'keyword' : request.data.get.}
        keywords = request.data.get('keyword')
        keyword_list = keywords.split() if keywords else []

        print(f"\n\n\nKeyword recieved: {keyword_list}\n\n\n")
        queryset = Artwork.objects.none()

        for kw in keyword_list:
            q_filter = (
                Q(title__icontains=kw) |
                Q(comments__icontains=kw) |
                Q(width__icontains=kw) |
                Q(height__icontains=kw) |
                Q(location__location__icontains=kw) |
                Q(donor__donor_name__icontains=kw) |
                Q(category__category__icontains=kw)
                # Add more fields here as needed
            )
            print(f"filter:{q_filter}")
            queryset |= Artwork.objects.filter(q_filter)
            print(f"Queryset: {queryset}")

        results = ArtworkSerializer(queryset, many=True)
        print(f"\n\n\nHere are some cool results: {results.data}\n\n\n")
        return Response(results.data, status=status.HTTP_200_OK)
