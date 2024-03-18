from rest_framework import serializers
from django.contrib.auth import get_user_model

from project.models import Lead

User = get_user_model()

class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'company_name', 'address', 'city', 'state', 'zip_code', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'company_name', 'address', 'city', 'state', 'zip_code']

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['id', 'user', 'name', 'date', 'phone', 'zip_code', 'insurance_company', 'status']
        read_only_fields = ('user',)