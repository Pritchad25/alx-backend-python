from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from .models import Message, MessageHistory, Notification, User

@receiver(pre_save, sender=Message)
def save_old_content_to_history(sender, instance, **kwargs):
    if instance.pk:
        try:
            old = Message.objects.get(pk=instance.pk)
            if old.content != instance.content:
                MessageHistory.objects.create(
                        message=old,
                        old_content=old.content,
                        changed_by=instance.edited_by,
                )
                instance.edited = True
        except Message.DoesNotExist:
            pass

@receiver(post_save, sender=Message)
def create_notification_on_message(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)

@receiver(post_delete, sender=User)
def delete_related_messages_and_notifications(sender, instance, **kwargs):
    messages_sent = Message.objects.filter(sender=instance)
    messages_received = Message.objects.filter(receiver=instance)

    for message in messages_sent | messages_received:
        MessageHistory.objects.filter(message=message).delete()

    messages_sent.delete()
    messages_received.delete()

    Notification.objects.filter(user=instance).delete()
