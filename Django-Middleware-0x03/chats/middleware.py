import datetime
import logging

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

