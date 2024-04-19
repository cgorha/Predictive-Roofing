from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from project.models import Conversation, ConversationMessage, CustomUser
from project.serializers import ConversationSerializer, ConversationDetailSerializer, ConversationMessageSerializer

@api_view(['GET'])
def conversation_list(request):
    conversations = Conversation.objects.filter(users__in=list([request.user]))
    serializer = ConversationSerializer(conversations,many=True)

    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def conversation_detail(request, pk):
    conversation = Conversation.objects.filter(users__in=list([request.user])).get(pk=pk)
    serializer = ConversationDetailSerializer(conversation)

    return JsonResponse(serializer.data, safe=False)

from rest_framework import status

@api_view(['POST'])
def conversation_send_message(request, pk):
    # Get the conversation associated with the given pk
    conversation = Conversation.objects.filter(users__in=[request.user]).get(pk=pk)
    
    # Determine the user to whom the message was sent
    for user in conversation.users.all():
        if user != request.user:
            sent_to = user

    # Create the conversation message
    conversation_message = ConversationMessage.objects.create(
        conversation=conversation,
        body=request.data.get('body'),
        created_by=request.user,
        sent_to=sent_to
    )

    # Check if the message was created by the current user
    if conversation_message.created_by == request.user:
        serializer = ConversationMessageSerializer(conversation_message)
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def send_message(request):
    if request.method == 'POST':
        # Extract necessary data from the request
        recipient_name = request.data.get('recipient_name')
        message_body = request.data.get('message_body')

        # Get the recipient user based on the provided name
        try:
            recipient_user = CustomUser.objects.get(username=recipient_name)
        except CustomUser.DoesNotExist:
            return JsonResponse({'error': f'User "{recipient_name}" not found'}, status=status.HTTP_404_NOT_FOUND)

        # Create a new conversation or retrieve an existing one
        conversation, created = Conversation.objects.get_or_create(users=[request.user, recipient_user])

        # Create the conversation message
        conversation_message = ConversationMessage.objects.create(
            conversation=conversation,
            body=message_body,
            created_by=request.user,
            sent_to=recipient_user
        )

        # Check if the message was created by the current user
        if conversation_message.created_by == request.user:
            serializer = ConversationMessageSerializer(conversation_message)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        # Method not allowed for other request methods
        return JsonResponse({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


