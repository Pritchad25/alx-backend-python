from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification

class MessageNotificationTest(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(username="sender", password="pass")
        self.receiver = User.objects.create_user(username="receiver", password="pass")

    def test_notification_created_on_new_message(self):
        message = Message.objects.create(
                sender=self.sender, receiver=self.receiver, content="Hello!"
        )
        notifications = Notification.objects.filter(user=self.receiver, message=message)
        self.assertEqual(notifications.count(), 1)
