from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from project.models import Lead, calendarEvent
from .serializers import UserSerializer, LeadSerializer, calendarEventSerializer

import os
from django.conf import settings
from django.http import HttpResponse

User = get_user_model()
class UserDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    class LeadListCreate(generics.ListCreateAPIView):
        serializer_class = LeadSerializer
        permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Lead.objects.filter(user=self.request.user)

class LeadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]

class calendarEventListCreate(generics.ListCreateAPIView):
    queryset = calendarEvent.objects.all()
    serializer_class = calendarEventSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    class calendarEventListCreate(generics.ListCreateAPIView):
        serializer_class = calendarEventSerializer
        permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return calendarEvent.objects.filter(user=self.request.user)

def send_sms(request):
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    twilio_phone_number = settings.TWILIO_PHONE_NUMBER

    message_body = request.POST.get('message')
    to_phone_number = request.POST.get('to_phone_number')
    client = Client(account_sid,auth_token)

    try:
        message = client.messages.create(
            body=message_body,
            from_=twilio_phone_number,
            to=to_phone_number
        )

        print(message.sid)
        return HttpResponse("SMS sent successfully")
    except Exception as e:
        # Return error response if sending SMS fails
        return HttpResponse(f"Error: {str(e)}", status=500)
    else:
        # Return error response if method is not POST
        return HttpResponse("Only POST requests are allowed", status=405)

