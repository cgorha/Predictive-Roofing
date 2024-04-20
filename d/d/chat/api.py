from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from project.models import Conversation, ConversationMessage, CustomUser
from project.serializers import ConversationSerializer, ConversationDetailSerializer, ConversationMessageSerializer
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def conversation_list(request):
    conversations = Conversation.objects.filter(users__in=[request.user])
    serializer = ConversationSerializer(conversations, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def conversation_detail(request, pk):
    conversation = Conversation.objects.filter(users__in=[request.user]).get(pk=pk)
    serializer = ConversationDetailSerializer(conversation)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def conversation_send_message(request, pk):
    conversation = Conversation.objects.filter(users__in=[request.user]).get(pk=pk)
    sent_to = next((user for user in conversation.users.all() if user != request.user), None)

    if not sent_to:
        return JsonResponse({'error': 'Recipient not found in the conversation.'}, status=status.HTTP_404_NOT_FOUND)

    conversation_message = ConversationMessage.objects.create(
        conversation=conversation,
        body=request.data.get('body'),
        created_by=request.user,
        sent_to=sent_to
    )

    serializer = ConversationMessageSerializer(conversation_message)
    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_message(request):
    recipient_name = request.data.get('recipient')
    message_body = request.data.get('body')

    try:
        recipient = CustomUser.objects.get(username=recipient_name)
        sender = request.user
        conversation, created = Conversation.objects.get_or_create()
        conversation.users.add(sender, recipient)

        message = ConversationMessage.objects.create(
            conversation=conversation,
            body=message_body,
            created_by=sender,
            sent_to=recipient
        )

        serializer = ConversationMessageSerializer(message)
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

    except CustomUser.DoesNotExist:
        return JsonResponse({'error': f'User "{recipient_name}" not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)