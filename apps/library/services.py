from typing import List

from django.db.models import QuerySet

from apps.library.models import PersonInPhoto, Photo


def create_person_from_list(*, names: List) -> List[PersonInPhoto]:
    return [PersonInPhoto.objects.get_or_create(name=name)[0] for name in names]


def assign_people_to_photo(*, photo: Photo, people: List[PersonInPhoto]) -> Photo:
    photo.people.add(*people)
    return photo
