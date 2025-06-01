from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Conversation, Message, CustomUser
from .serializers import ConversationSerializer, MessageSerializer
from rest_framework.decorators import action

class ConversationViewSet(viewsets.ModelViewSet):
    """ViewSet for handling conversations."""
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    @action(detail=False, methods=['post'])
    def create_conversation(self, request):
        """Creates a new conversation between users."""
        user_ids = request.data.get("participants", [])
        users = CustomUser.objects.filter(id__in=user_ids)

        if len(users) < 2:
            return Response({"error": "A conversation needs at least two participants."},
                         status=status.HTTP_400_BAD_REQUEST)

        conversation = Conversation.objects.create()
        conversation.participants.set(users)
        conversation.save()

        return Response(ConversationSerializer(conversation).data, status=status.HTTP_201_CREATED)

class MessageViewSet(viewsets.ModelViewSet):
    """ViewSet for handling messages within conversations."""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    @action(detail=False, methods=['post'])
    def send_message(self, request):
        """Sends a message in an existing conversation."""
        conversation_id = request.data.get("conversation_id")
        sender_id = request.data.get("sender_id")
        content = request.data.get("content")

        try:
            conversation = Conversation.objects.get(id=conversation_id)
            sender = CustomUser.objects.get(id=sender_id)
        except (Conversation.DoesNotExist, CustomUser.DoesNotExist):
            return Response({"error": "Invalid conversation or sender ID."}, 
                    status=status.HTTP_400_BAD_REQUEST)

        message = Message.objects.create(conversation=conversation, sender=sender, content=content)

        return Response(MessageSerializer(message).data, status=status.HTTP_201_CREATED)
# Create your views here.
