import time

from django.urls import resolve

from libs.tracing.django_logger import DjangoLogging
from libs.urls.resolvers import ResolverMatch


class Tracer:
    def __init__(self, handler, _logger=None):
        self.handler = handler
        self._logger = _logger

    @property
    def logger(self):
        return self._logger


class TracerMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        matched_handler: ResolverMatch = resolve(request.path_info)
        start = time.time()
        logger = DjangoLogging.init(handler=matched_handler.function_name)
        logger.debug(f"==================== Start tracing for {matched_handler.function_name} handler  ====================")
        setattr(request, "tracer", Tracer(handler=matched_handler.function_name, _logger=logger))
        response = self.get_response(request)
        logger.debug(f"==================== End tracing for {matched_handler.function_name} handler - Consolidated execution time to handle {time.time() - start}s ====================")

        return response
