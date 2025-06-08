import django_filters
from .models import Message

class MessageFilter(django_filters.FilterSet):
    sender = django_filters.CharFilter(field_name="sender__username", lookup_expr="iexact")
    receiver = django_filters.CharFilter(field_name="receiver__username", lookup_expr="iexact")
    timestamp = django_filters.DateTimeFromToRangeFilter(field_name="timestamp")

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'timestamp']
