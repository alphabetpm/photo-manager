from rest_framework import viewsets

from apps.library.models import Photo
from apps.library.serializers import PhotoListSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoListSerializer
