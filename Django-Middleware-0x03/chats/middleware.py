import datetime
import logging
from django.http import HttpResponseForbidden
from collections import defaultdict

class OffensiveLanguageMiddleware:
    """
    Middleware to restrict users from sending more than 5 messages per minute based on their IP address.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.message_tracker = defaultdict(list)  # Tracks timestamps per IP

    def __call__(self, request):
        if request.method == "POST" and request.path.startswith("/api/messages/"):
            user_ip = self.get_client_ip(request)
            current_time = time.time()

            # Remove timestamps older than 60 seconds
            self.message_tracker[user_ip] = [
                    timestamp for timestamp in self.message_tracker[user_ip]
                    if current_time - timestamp < 60
            ]

            # Check if user exceeded the limit
            if len(self.message_tracker[user_ip]) >= 5:
                return HttpResponseForbidden("You have exceeded the message limit (5 per minute). Please wait.")

            # Log new message timestamp
            self.message_tracker[user_ip].append(current_time)
        return self.get_response(request)

    def get_client_ip(self, request):
        """ Extracts IP address from request headers """
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0].strip()
        return request.META.get("REMOTE_ADDR")

class RestrictAccessByTimeMiddleware:
    """
    Middleware to restrict access to the messaging app outside 9 AM - 6 PM.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_time = datetime.datetime.now().time()
        start_restricted_time = datetime.time(21, 0) # 9PM
        end_restricted_time = datetime.time(6, 0) #6AM
        if not (start_restricted_time <= current_time or current_time < end_restricted_time):
            return HttpResponseForbidden("Access to messaging app is restricted outside 9 AM - 6 PM.")
        return self.get_response(request)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        logging.basicConfig(
                filename="requests.log",
                level=logging.INFO,
                format="%(message)s",
        )

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        log_message = f"{datetime.datetime.now()} - User: {user} - Path: {request.path}"
        logging.info(log_message)

        response = self.get_response(request)
        return response

