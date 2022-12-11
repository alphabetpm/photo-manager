from django.contrib import admin

from apps.library.models import Photo, PersonInPhoto


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ["id", "file", "owner", "created_at"]


@admin.register(PersonInPhoto)
class PersonInPhotoAdmin(admin.ModelAdmin):
    list_display = ["name"]
