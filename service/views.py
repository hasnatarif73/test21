from rest_framework import viewsets,filters
from .models import Service, Jobs
from .serializers import ServiceSerializer, JobsSerializer
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['service_title']       # ✅ Filter services by title
    search_fields = ['service_title', 'service_description']  # ✅ Full-text search
    ordering_fields = ['service_title']        # ✅ Sorting alphabetically

class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer
    permission_classes = [IsAdminOrReadOnly]
    # For django-filter
    filterset_fields = ['job_title']  # fields you want to allow filtering by

    # For search filter
    search_fields = ['job_title', 'job_description']  # enable ?search=

    # For ordering
    ordering_fields = ['job_title']  # allow ?ordering=job_title
