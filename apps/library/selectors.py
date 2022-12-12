from typing import List

from apps.library.models import PersonInPhoto


def get_people_names_by_keyword_in_list(keyword: str) -> List[str]:
    qs = PersonInPhoto.objects.filter(name__icontains=keyword)
    return [person.name for person in qs]
