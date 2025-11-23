from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserFormViewSet

router = DefaultRouter()
router.register(r'user-forms', UserFormViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
