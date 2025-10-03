import traceback

from rest_framework import status
from rest_framework.authentication import get_authorization_header

from libs.exceptions.authentication import AuthenticationException, AuthorizationNotProvidedException, \
    UnauthenticatedClient
from libs.http_client.authentication import ClientAuthentication
from libs.responses import APIResponse
from libs.tracing.django_logger import DjangoLogging
from libs.ultils import get_func_patch_name


class AuthenticationMiddleware:
    EXCLUDED_PATHS = [
        "/api-docs/",
        "/redoc/",
        "/static/",
        "/storage/",

        "/products/v1/create",
        "/products/v1/products",
        "/products/v1/product/",
        "/products/v1/update/",
        "/products/v1/delete/",
        "/products/v1/uploads/",
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if any(request.path.startswith(path) for path in self.EXCLUDED_PATHS):
            return self.get_response(request)
        tracer = request.tracer if hasattr(request, "tracer") else None
        handler = get_func_patch_name(f=self.__call__)
        logger = DjangoLogging.init(handler=handler, logger=tracer.logger) if tracer else DjangoLogging.init(
            handler=handler)
        auth = get_authorization_header(request).split()
        _response = APIResponse(handler=handler)
        try:
            if not auth or auth[0].lower() != b'bearer':
                raise AuthorizationNotProvidedException()
            token = auth[1].decode('utf-8')
            logger.debug(f"AuthenticationMiddleware: {auth}")
            if token:
                payload_token = ClientAuthentication.authentication(token)
                setattr(request, "payload", payload_token)

        except Exception as e:
            if isinstance(e, AuthenticationException):
                logger.error(f"AuthenticationMiddleware: {e.message}")
                _response.check_message(e.message)
                _response.add_errors({
                    "header": {
                        "message": f"AuthenticationMiddleware: {e.message}"
                    }
                })
                _response.check_code(1403)
                return _response.render(http_code=e.status_code)
            else:
                _response.check_message(str(e))
                _response.add_errors({
                    "header": {
                        "message": f"AuthenticationMiddleware: Unknown error - {e}"
                    }
                })
                logger.error(f"AuthenticationMiddleware: {e}")
                _response.render(http_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        response = self.get_response(request)
        return response
