from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """Custom User model extending Django's default User model."""
    bio = models.TextField(blank=True, null=True)

class Conversation(models.Model):
    """Model to track user conversations."""
    participants = models.ManyToManyField(CustomUser,
                                      related_name="conversations")
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    """Model for messages sent in a conversation."""
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
