from rest_framework import status


class SimpleBaseException(Exception):
    def __init__(self, message='', error=None, status_code=status.HTTP_400_BAD_REQUEST):
        self.message = message
        self.error = {} if not error else error
        self.status_code = status_code
        super(SimpleBaseException, self).__init__(message)


class APIWarningException(SimpleBaseException):
    def __init__(self, message="API Warning Exception", error=None, status_code=1400, http_code=status.HTTP_200_OK):
        self.message = message
        self.error = error if error else {}
        self.status_code = status_code
        self.http_code = http_code
        super(APIWarningException, self).__init__(self.message, self.error, self.status_code)

    pass


class DictResultBlockInfinityException(SimpleBaseException):
    def __init__(self, error=None, status_code=status.HTTP_400_BAD_REQUEST):
        self.message = "Dict result has been block infinity"
        self.error = {} if not error else error
        self.status_code = status_code
        super(DictResultBlockInfinityException, self).__init__(self.message, self.error, self.status_code)


class ExpiredTokenException(APIWarningException):
    def __init__(self, ):
        super().__init__(
            message="Token has expired",
            status_code=1500,
            error={}
        )
