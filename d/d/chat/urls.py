from django.urls import path
from . import api

urlpatterns = [
    path('', api.conversation_list, name='conversation_list'),
    path('<int:pk>/', api.conversation_detail, name='conversation_detail'),
    path('<int:pk>/send/', api.conversation_send_message, name='conversation_send_message'),
    path('send/', api.send_message, name='send_message'),
]
