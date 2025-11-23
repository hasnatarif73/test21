from rest_framework import viewsets
from .models import userForm
from .serializers import UserFormSerializer

class UserFormViewSet(viewsets.ModelViewSet):
    queryset = userForm.objects.all()
    serializer_class = UserFormSerializer
