from rest_framework.routers import DefaultRouter

from apps.library.views import PhotoViewSet

router = DefaultRouter()
router.register("photo", PhotoViewSet)


urlpatterns = []
urlpatterns += router.urls
