from rest_framework import status

from libs.exceptions.commons import SimpleBaseException


class AuthenticationException(SimpleBaseException):
    def __init__(self, message="Authentication API not provide"):
        self.message = message
        self.error = "authentication_error"
        self.status_code = status.HTTP_403_FORBIDDEN
        super(AuthenticationException, self).__init__(self.message, self.error, self.status_code)


class UnauthenticatedClient(AuthenticationException):
    def __init__(self, message="Unauthenticated Client"):
        self.message = message
        self.error = "authentication_error"
        self.status_code = status.HTTP_403_FORBIDDEN
        super(UnauthenticatedClient, self).__init__(self.message)


class AuthorizationNotProvidedException(AuthenticationException):
    def __init__(self, message="Authorization header not provide"):
        self.message = message
        self.error = "authorization_not_provided"
        self.status_code = status.HTTP_403_FORBIDDEN
        super(AuthorizationNotProvidedException, self).__init__(self.message)
