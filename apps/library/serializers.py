from django.db import transaction

from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from apps.library.models import Photo, PersonInPhoto
from apps.library.services import create_person_from_list, assign_people_to_photo


class PersonInPhotoTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonInPhoto
        fields = ("name",)


class PhotoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ("id", "file")


class PhotoCreateSerializer(serializers.ModelSerializer):
    file = Base64ImageField(required=True)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    people = serializers.ListSerializer(child=serializers.CharField(), required=False)

    def validate_people(self, value):
        return create_person_from_list(names=value)

    @transaction.atomic
    def create(self, validated_data):
        people = validated_data.pop("people", None)
        photo: Photo = super().create(validated_data)
        if people:
            assign_people_to_photo(photo=photo, people=people)
        return photo

    class Meta:
        model = Photo
        fields = (
            "id",
            "file",
            "description",
            "people",
            "owner",
            "latitude",
            "longitude",
        )
        read_only_fields = ("id",)


class PhotoRetrieveSerializer(serializers.ModelSerializer):
    people = serializers.StringRelatedField(many=True)

    class Meta:
        model = Photo
        fields = ("id", "file", "description", "people", "latitude", "longitude")


class SearchPersonByNameSerializer(serializers.Serializer):
    keyword = serializers.CharField()
