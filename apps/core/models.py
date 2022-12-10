from django.db import models

# Create your models here.
class LocationAbstractModel(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def location(self):
        return self.latitude, self.longitude

    def __str__(self) -> str:
        return f"{self.latitude}, {self.longitude}"

    class Meta:
        abstract = True


class CreatedAtAbstract(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UpdatedAtAbstract(models.Model):
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CreatedUpdatedAtAbstract(CreatedAtAbstract, UpdatedAtAbstract):
    class Meta:
        abstract = True
        ordering = ["-created_at"]
