import json
from enum import Enum

from rest_framework import status
from rest_framework.compat import SHORT_SEPARATORS, INDENT_SEPARATORS, LONG_SEPARATORS
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from libs.shared.entities import BaseEntity


class JsonApiRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if data is None:
            return b''

        renderer_context = renderer_context or {}
        indent = self.get_indent(accepted_media_type, renderer_context)

        if indent is None:
            separators = SHORT_SEPARATORS if self.compact else LONG_SEPARATORS
        else:
            separators = INDENT_SEPARATORS

        ret = json.dumps(
            data, cls=self.encoder_class,
            indent=indent, ensure_ascii=self.ensure_ascii,
            allow_nan=not self.strict, separators=separators,
            default=self.default
        )
        ret = ret.replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')
        return ret.encode()

    @staticmethod
    def default(obj):
        if isinstance(obj, BaseEntity):
            return obj.to_dict()
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        if isinstance(obj, Enum):
            return obj.name
        raise Exception(f"Type {type(obj)} is not JSON serializable")


class APIResponse:
    def __init__(self, handler, **kwargs):
        self.handler = handler
        self.code_status = 0
        self.message = ""
        self.errors = {}
        self.data_resp = {}
        self.kwargs = kwargs

    def check_message(self, message):
        self.message = self.message or message

    def check_code(self, code_status):
        self.code_status = self.code_status or code_status

    def add_errors(self, error):
        if isinstance(error, list):
            self.errors = error
        if isinstance(error, dict) and isinstance(self.errors, dict):
            self.errors.update(error)

    def get_code(self, code=1200):
        return self.code_status or code

    def make_format(self):
        code_status = self.get_code(1400 if self.errors else 1200)
        message = self.message or ('Success' if not self.errors else '')
        data = self.data_resp if isinstance(self.data_resp, dict) else {"data": self.data_resp}
        return dict(
            success=not bool(self.errors),
            message=message, code_status=code_status,
            result=data,
            error=self.errors, **self.kwargs
        )

    def make_response(self, http_code=None):
        return Response(self.make_format(), status=http_code if http_code else status.HTTP_200_OK)

    def render(self, http_code=None):
        response = self.make_response(http_code)
        response.accepted_renderer = JsonApiRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        response.render()
        return response


class PaginatorResponse(APIResponse):
    def __init__(self, handler, **kwargs):
        super().__init__(handler, **kwargs)
        self.limit = None
        self.offset = None
        self.total_items = None

    def make_format(self):
        response = super().make_format()
        limit = self.limit
        offset = self.offset
        total_items = self.total_items
        response["limit"] = limit
        response["offset"] = offset
        response["total_items"] = total_items
        return response
