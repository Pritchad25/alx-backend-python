from django.contrib import admin
from .models import Message, MessageHistory


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["sender", "receiver", "content", "edited", "sent_at"]

@admin.register(MessageHistory)
class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ["message", "changed_at", "old_content"]
