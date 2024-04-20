from rest_framework import serializers
from django.contrib.auth import get_user_model

from project.models import Lead
from .models import Conversation, ConversationMessage, calendarEvent

User = get_user_model()

class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'company_name', 'address', 'city', 'state', 'zip_code', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print("Validated data:", validated_data)
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

class calendarEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = calendarEvent
        fields = ['id', 'user', 'title', 'start', 'description']
        read_only_fields = ('user',)

class ConversationSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True, many=True)
    modified_at_formatted = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ('id', 'users', 'modified_at_formatted')

    def get_modified_at_formatted(self, obj):
        return obj.modified_at.strftime('%Y-%m-%d %H:%M:%S')  # Format the datetime as a string

class ConversationMessageSerializer(serializers.ModelSerializer):
    sent_to = UserSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = ConversationMessage
        fields = ('id', 'sent_to','created_by','created_at_formatted','body')

class ConversationDetailSerializer(serializers.ModelSerializer):
    messages = ConversationMessageSerializer(read_only=True, many=True)

    class Meta:
        model = Conversation
        fields = ('id','users','modified_at_formatted','messages',)

class ConversationSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True, many=True)
    modified_at_formatted = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ('id', 'users', 'modified_at_formatted')

    def get_modified_at_formatted(self, obj):
        return obj.modified_at.strftime('%Y-%m-%d %H:%M:%S')  # Format the datetime as a string

class ConversationMessageSerializer(serializers.ModelSerializer):
    sent_to = UserSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = ConversationMessage
        fields = ('id', 'sent_to','created_by','created_at_formatted','body')

class ConversationDetailSerializer(serializers.ModelSerializer):
    messages = ConversationMessageSerializer(read_only=True, many=True)

    class Meta:
        model = Conversation
        fields = ('id','users','modified_at_formatted','messages',)