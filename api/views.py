from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from django.db.models import Q
from django.conf import settings

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    @action(detail=False, methods=['GET'])
    def get_user_by_email(self, request):
        email = request.query_params.get('email', None)

        if email is None:
            return Response({'error': 'Email parameter is required'}, status=400)

        user = get_object_or_404(CustomUser, email=email)

        serializer = self.get_serializer(user)
        return Response(serializer.data)

class MigrationRequestViewSet(viewsets.ModelViewSet):
    queryset = MigrationRequest.objects.all()
    serializer_class = MigrationRequestSerializer

    def get_queryset(self):
        email = self.request.query_params.get('email', None)
        if email is not None:
            # Filter MigrationRequests based on the provided email
            return MigrationRequest.objects.filter(email=email)
        return MigrationRequest.objects.all()

class ArtworkImageViewSet(viewsets.ModelViewSet):
    queryset = ArtworkImage.objects.all()
    serializer_class = ArtworkImageSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        image_url = f"{settings.AWS_S3_CUSTOM_DOMAIN}/{instance.image_file.name}"
        return Response({'image_url': image_url, 'data': serializer.data})
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class DonorViewSet(viewsets.ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
