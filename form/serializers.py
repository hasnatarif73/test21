from rest_framework import serializers
from .models import userForm

class UserFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = userForm
        fields = '__all__'
