from django_filters import FilterSet
from django_filters import rest_framework as filters

from apps.library.models import Photo


class PhotoFilterSet(FilterSet):
    people = filters.CharFilter(method="filter_people")
    created_at = filters.DateFilter(method="filter_created_at")

    def filter_people(self, qs, name, value, *args, **kwargs):
        return qs.filter(people__name__icontains=value)

    def filter_created_at(self, qs, name, value, *args, **kwargs):
        return qs.filter(created_at__date=value)

    class Meta:
        model = Photo
        fields = ("created_at", "people", "latitude", "longitude")
