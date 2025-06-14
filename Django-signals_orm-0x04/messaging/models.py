import uuid
from django.db import models
from django.contrib.auth.models import User
from .managers import UnreadMessagesManager

class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(
         User, on_delete=models.CASCADE, related_name="messages_sent"
    )
    receiver = models.ForeignKey(
         User, on_delete=models.CASCADE, related_name="messages_received"
    )
    parent_message = models.ForeignKey(
         "self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    read = models.BooleanField(default=False)
    edited_at = models.DateTimeField(null=True, blank=True)
    edited_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="messages_edited",
    )
    objects = models.Manager()
    unread = UnreadMessagesManager()

    def __str__(self):
        return (
           f"{self.sender.username} -> {self.receiver.username}: {self.content[:30]}"
        )

class MessageHistory(models.Model):
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name="history"
    )
    old_content = models.TextField()
    changed_at = models.DateTimeField(auto_now_add=True)
    changed_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"History for message {self.message.id} at {self.changed_at}"

class Notification(models.Model):
    user = models.ForeignKey(
      User, on_delete=models.CASCADE, related_name="notifications"
    )
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"
