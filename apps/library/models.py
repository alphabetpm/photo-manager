from django.db import models
from django.contrib.auth import get_user_model
from apps.core.models import LocationAbstractModel, CreatedUpdatedAtAbstract


class Photo(LocationAbstractModel, CreatedUpdatedAtAbstract):
    file = models.ImageField(upload_to="photo")
    description = models.TextField(null=True, blank=True)
    people = models.ManyToManyField("library.PersonInPhoto")
    owner = models.ForeignKey(
        get_user_model(), related_name="photos", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.owner}, {self.id}"


class PersonInPhoto(CreatedUpdatedAtAbstract):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
