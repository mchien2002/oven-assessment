import datetime
import json
import logging
from django.conf import settings


class DjangoFormatter(logging.Formatter):

    @staticmethod
    def get_extra(record, attr):
        if hasattr(record, attr):
            return getattr(record, attr)
        return ""

    def format(self, record: logging.LogRecord) -> str:
        log_data = {
            "system.timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "logger": record.name,
            "handler": self.get_extra(record, "handler"),
            "tracer": self.get_extra(record, "tracer"),
            "file": record.filename,
            "module": record.module,
            "func.name": record.funcName,
            "application.time": self.get_extra(record, "application_time"),
            "line.no": record.lineno,
            "message": record.getMessage(),
        }
        if hasattr(settings, "LOG_FORMAT") and settings.LOG_FORMAT == "json":
            return json.dumps(log_data, ensure_ascii=False)
        return super().format(record)

    def formatTime(self, record, datefmt=None):
        dt = datetime.datetime.fromtimestamp(record.created)
        if datefmt:
            return dt.strftime(datefmt)
        else:
            # ISO 8601
            return dt.isoformat(timespec='milliseconds')
