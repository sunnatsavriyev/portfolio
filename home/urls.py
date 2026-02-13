from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MurojaatViewSet

router = DefaultRouter()
router.register("murojaat", MurojaatViewSet, basename="murojaat")

urlpatterns = [
    path("api/", include(router.urls)),
]
