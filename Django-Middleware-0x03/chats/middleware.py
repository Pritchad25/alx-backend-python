import datetime
import logging
from django.http import HttpResponseForbidden

class RestrictAccessByTimeMiddleware:
    """
    Middleware to restrict access to the messaging app outside 9 AM - 6 PM.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_time = datetime.datetime.now().time()
        start_restricted_time = datetime.time(9, 0) #9AM
        end_restricted_time = datetime.time(18, 0) #6PM

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

