from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, JobsViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'jobs', JobsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
