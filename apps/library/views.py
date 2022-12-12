from rest_framework import viewsets, views
from rest_framework.response import Response

from apps.library.models import Photo, PersonInPhoto
from apps.library.serializers import (
    PhotoListSerializer,
    PhotoCreateSerializer,
    PhotoRetrieveSerializer,
    SearchPersonByNameSerializer,
)
from apps.library.filters import PhotoFilterSet
from apps.library.selectors import get_people_names_by_keyword_in_list


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoListSerializer
    filterset_class = PhotoFilterSet

    def get_serializer_class(self):
        if self.action == "create":
            self.serializer_class = PhotoCreateSerializer
        elif self.action == "retrieve":
            self.serializer_class = PhotoRetrieveSerializer
        elif self.action == "list":
            self.serializer_class = PhotoListSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user)


class SearchPersonByNameView(views.APIView):
    queryset = PersonInPhoto.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = SearchPersonByNameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            get_people_names_by_keyword_in_list(
                keyword=serializer.validated_data["keyword"]
            )
        )
