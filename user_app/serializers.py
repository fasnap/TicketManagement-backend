from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Username already exists")
        
        return data
    def create(self, validated_data):
        validated_data.pop('confirm_password')

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user