from rest_framework import serializers
from .models import CustomUser

class CusomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password']

    # Create a new user function
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)