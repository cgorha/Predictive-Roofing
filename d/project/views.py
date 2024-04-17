from venv import logger

from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from requests import Response
from rest_framework.response import Response

from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


from project.models import Lead, calendarEvent, MapPin
from rest_framework.utils import json

from .serializers import UserSerializer, LeadSerializer, calendarEventSerializer

import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse

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

@require_POST
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_pin(request):
    try:
        data = json.loads(request.body)
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'User is not authenticated'}, status=401)

        pin = MapPin.objects.create(user=request.user, latitude=data['latitude'], longitude=data['longitude'], description=data.get('description', ''))
        logger.info(f"Pin saved: {pin}")
        return JsonResponse({"message": "Pin saved successfully", "id": pin.id}, status=201)
    except Exception as e:
        logger.error(f"Error saving pin: {str(e)}")
        return JsonResponse({"error": str(e)}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_pins(request):
    try:
        pins = MapPin.objects.filter(user=request.user)
        data = [{"latitude": pin.latitude, "longitude": pin.longitude, "description": pin.description} for pin in pins]
        return Response(data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

