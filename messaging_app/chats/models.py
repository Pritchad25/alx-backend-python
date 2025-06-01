from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Custom user model extending Django's default User model."""
    bio = models.TextField(blank=True, null=True)  # Example additional field

    # Fixing reverse accessor clashes by adding unique `related_name`
    groups = models.ManyToManyField("auth.Group", related_name="customuser_groups")
    user_permissions = models.ManyToManyField(
            "auth.Permission", related_name="customuser_permissions")

class Conversation(models.Model):
    """Tracks user conversations."""
    participants = models.ManyToManyField(CustomUser,
                      related_name="conversations")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation between {', '.join([p.username for p in self.participants.all()])}"

class Message(models.Model):
    """Stores messages exchanged in a conversation."""
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} at {self.timestamp}"
