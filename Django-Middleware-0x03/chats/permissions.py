from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Allows access only to authenticated users who are participants in the
    conversation.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        ## Ensure the user is a participant in the conversation
        if obj.sender == request.user or obj.receiver == request.user:
            # Restrict methods explicitly
            if request.method in ["PUT", "PATCH", "DELETE"]:
                return obj.sender == request.user  # Only sender can modify/delete messages
            return True  # Allow GET, POST requests for participan
        return False #tsr
