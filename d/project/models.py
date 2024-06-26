from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils.timesince import timesince


class CustomUser(AbstractUser):
    company_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=12, blank=True, null=True)


class Lead(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='leads')
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    zip_code = models.CharField(max_length=12)
    insurance_company = models.CharField(max_length=255)
    status = models.CharField(max_length=100)


class calendarEvent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events')
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    start = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.name

class MapPin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='map_pins')
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.address} ({self.latitude}, {self.longitude})"

class Conversation(models.Model):
    users = models.ManyToManyField(CustomUser, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def modified_at_formatted(self):
        return timesince(self.modified_at)

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    body = models.TextField()
    sent_to = models.ForeignKey(CustomUser, related_name='received_messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, related_name='sent_messages', on_delete=models.CASCADE)

    def created_at_formatted(self):
        return timesince(self.created_at)