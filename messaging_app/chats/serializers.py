from rest_framework import serializers
from .models import CustomUser, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    """Serializer for CustomUser model."""
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio']

class MessageSerializer(serializers.ModelSerializer):
    """Serializer for Message model."""
    sender = UserSerializer(read_only=True)
    class Meta:
        model = Message
        fields = ['id', 'sender', 'conversation', 'content', 'timestamp']

class ConversationSerializer(serializers.ModelSerializer):
    """Serializer for Conversation model, including nested messages."""
    participants = UserSerializer(many=True, read_only=True)  # Include participants
    messages = MessageSerializer(many=True, source="message_set", read_only=True)  # Include messages

    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'messages', 'created_at']

