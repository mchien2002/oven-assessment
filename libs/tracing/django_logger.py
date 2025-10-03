import datetime
import logging
import uuid

from django.conf import settings


class DjangoLogging:
    def __init__(self, logger=None, handler="", tracer=None, service_name=None):
        self._logger = self.get_logger(logger)
        self.handler = handler
        self.tracer = f"tracer-{uuid.uuid1().hex}" if not tracer else tracer
        self.service_name = service_name if service_name else settings.SERVICE_NAME

    @property
    def logger(self):
        return self._logger

    @staticmethod
    def get_logger(logger=None):
        return logger if isinstance(logger, (logging.Logger, logging.RootLogger)) else logging.getLogger(logger or "")

    def log(self, lv, message, handler=""):
        log_message = {
            "handler": self.handler if not handler else handler,
            "tracer": self.tracer,
            "application_time": f"{datetime.datetime.now()}"
        }
        self.logger.log(getattr(logging, lv.upper(), 0), message, extra=log_message, stacklevel=3)

    def info(self, message):
        self.log("info", message)

    def error(self, message):
        self.log("error", message)

    def warning(self, message):
        self.log("warning", message)

    def debug(self, message):
        self.log("info", message)

    @classmethod
    def init(cls, handler, logger=None, service_name=""):
        if not logger:
            return cls(handler=handler, service_name=service_name)
        if isinstance(logger, cls):
            return cls(handler=handler, logger=logger.logger,
                       tracer=logger.tracer, service_name=service_name)
        return cls(handler=handler, logger=logger, service_name=service_name)
