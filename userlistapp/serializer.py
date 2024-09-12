from rest_framework import serializers
from .models import UserListModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserListModel
        fields = '__all__'