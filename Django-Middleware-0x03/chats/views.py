from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import MessagePagination
from .filters import MessageFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsParticipantOfConversation
from .models import Conversation, Message, CustomUser
from .serializers import ConversationSerializer, MessageSerializer
from rest_framework.decorators import action

class ConversationViewSet(viewsets.ModelViewSet):
    """ViewSet for handling conversations."""
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]

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
    serializer_class = MessageSerializer
    permission_classes = [IsParticipantOfConversation]
    pagination_class = MessagePagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = MessageFilter

    def get_queryset(self):
        """
        Ensure users can only retrieve messages they are participants in.
        """
        user = self.request.user
        return Message.objects.filter(sender=user) | Message.objects.filter(receiver=user)

    def destroy(self, request, *args, **kwargs):
        """
        Ensure only the sender can delete a message.
        """
        message = self.get_object()
        if message.sender != request.user:
            return Response({"detail": "You are not allowed to delete this message."}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

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
