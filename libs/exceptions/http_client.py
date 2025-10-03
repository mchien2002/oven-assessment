from rest_framework import status
import requests

from libs.exceptions.commons import SimpleBaseException


class HTTPUnsuccessfulException(SimpleBaseException):
    def __init__(self, message="HTTP request unsuccessful", status_code=status.HTTP_400_BAD_REQUEST):
        self.message = message
        self.error = "api_call_error"
        self.status_code = status_code
        super(HTTPUnsuccessfulException, self).__init__(self.message, self.error, self.status_code)

    @classmethod
    def from_response(cls, response: requests.Response):
        message = f"HTTP request unsuccessful with status code {response.status_code}"
        if response.status_code != status.HTTP_200_OK:
            raise cls(message, response.status_code)