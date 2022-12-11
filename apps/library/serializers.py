from rest_framework import serializers

from apps.library.models import Photo


class PhotoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ("id", "file")
