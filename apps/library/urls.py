from django.urls import path

from rest_framework.routers import DefaultRouter

from apps.library.views import PhotoViewSet, SearchPersonByNameView

router = DefaultRouter()
router.register("photo", PhotoViewSet)


urlpatterns = [
    path("search/", SearchPersonByNameView.as_view(), name="search_names_by_keyword")
]
urlpatterns += router.urls
