from django.contrib import admin
from .models import CustomUser, Conversation, Message

admin.site.register(CustomUser)
admin.site.register(Conversation)
admin.site.register(Message)

# Register your models here.
