import traceback
from functools import wraps

from django.conf import settings
from django.views.decorators.http import require_http_methods
from rest_framework import status
from rest_framework.decorators import api_view

from libs.exceptions.commons import APIWarningException
from libs.responses import APIResponse
from libs.tracing.django_logger import DjangoLogging
from libs.ultils import get_func_patch_name


def content_type_api(allow_content_type, request):
    if "__all__" not in allow_content_type:
        not_contain = True
        for content_type in allow_content_type:
            if content_type in request.content_type:
                not_contain = False
        if not_contain:
            return False
    return True


def pretty_api(
        http_methods,
        class_response=APIResponse,
        allow_content_type=("__all__",),
        serializer=None,
):
    def decorator(func):
        @api_view(http_methods)  # Thêm api_view từ DRF
        @require_http_methods(http_methods)
        @wraps(func)
        def inner(request, **kwargs):
            view_handler = get_func_patch_name(f=func)
            _response = class_response(handler=view_handler)
            default_status_code = status.HTTP_200_OK
            kwargs.update(_response=_response)
            tracer = request.tracer if hasattr(request, "tracer") else None
            p_logger = tracer.logger if tracer else ""
            logger = DjangoLogging.init(handler=view_handler, logger=p_logger)
            if not content_type_api(allow_content_type, request):
                _response.check_message('Content-type has incorrect format')
                _response.add_errors({
                    "header": {
                        "message": f"Content-type has incorrect format. It must be one of {allow_content_type}"
                    }
                })
                _response.check_code(1406)
                return _response.make_response(http_code=status.HTTP_406_NOT_ACCEPTABLE)
            kwargs.update(request=request, data_serialized=None, logger=logger)
            if serializer:
                data_serialized = serializer(data=request.data)
                if not data_serialized.is_valid():
                    _response.check_message('Data input is invalid.')
                    _response.check_code(1400)
                    _response.add_errors({
                        "serializer": {
                            "errors": data_serialized.errors
                        }
                    })
                    return _response.make_response(http_code=status.HTTP_400_BAD_REQUEST)
                kwargs.update(data_serialized=data_serialized.data)
            try:
                logger.debug(f"Request header: {request.headers}")
                logger.debug(f"Request query params: {request.query_params.dict()}")
                logger.debug(f"Request data: {request.data}")
                func(**kwargs)
            except Exception as e:
                if isinstance(e, APIWarningException):
                    logger.error(message=f"APIWarningException error: {e}")
                    _response.check_message(e.message)
                    _response.add_errors(e.error)
                    _response.add_errors({
                        "PredictableError": {
                            "name": e.__class__.__name__,
                        }
                    })
                    _response.check_code(e.status_code)
                    default_status_code = e.http_code
                else:
                    if settings.DEBUG:
                        print(traceback.format_exc())
                    logger.error(message=f"Unpredictable exception error: {e}")
                    logger.error(message=f"Stack trace {traceback.format_exc()}")
                    _response.check_message('Ops! Something were wrong.')
                    _response.check_code(1400)
                    _response.add_errors({"unknown_error": {
                        'field': "",
                        'message': 'An error occurred. Please try again later.' if not _response.message else _response.message
                    }})
                    logger.warning(f"Error: {str(e)}")
                    default_status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return _response.render(http_code=default_status_code)

        return inner

    return decorator


def pretty_function():
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            logger = None
            new_args = []
            for arg in args:
                if isinstance(arg, DjangoLogging):
                    logger = arg
                else:
                    new_args.append(arg)
            logger = kwargs.get("logger", None) or logger
            logger = DjangoLogging.init(handler=get_func_patch_name(f=func), logger=logger)
            kwargs.update(logger=logger)
            return func(*new_args, **kwargs)

        return inner

    return decorator
