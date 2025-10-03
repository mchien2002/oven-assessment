from typing import Optional, Dict, Any

import requests

from libs.tracing.decorator import pretty_function


class HTTPService:
    POST = "post"
    GET = "get"
    PUT = "put"

    def __init__(self, protocol: str, host_name: str, service_name: str = "", header: Optional[Dict[str, str]] = None, cert: bool = True, response_log: bool = False):
        self.service_name = service_name
        self._host_name = host_name
        self.protocol = protocol
        self.cert = cert
        self.default_header = header or {}
        self.url = f"{self.protocol}://{self._host_name}"
        self.requests = requests.Session()
        self.response_log = response_log

    def get_header(self, header: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        return {**self.default_header, **(header or {})}

    @pretty_function()
    def fetch(self, uri: str = '', body: Optional[Dict[str, Any]] = None, files: Optional[Dict[str, Any]] = None, logger: Any = None, header: Optional[Dict[str, str]] = None, method: str = "post", timeout: int = 15, params: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        full_url = f"{self.url}{uri}" if uri.startswith("/") else f"{self.url}/{uri}"
        func_call = getattr(self.requests, method)
        header = self.get_header(header)
        api_name = uri.replace("/", "_").replace("-", "_")
        logger.debug(f"call {api_name} with url {full_url} body {body}")
        data = {
            "success": False
        }
        body = body or {}

        try:
            response = func_call(full_url, json=body, headers=header, files=files, verify=self.cert, timeout=timeout, params=params or {})
            data.update(http_status=response.status_code)
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"call {api_name} error with {e}")
        else:
            try:
                data.update({"response": response.json()})
                data["success"] = True
            except ValueError as e:
                logger.error(f"parse data error with {response.content} and exception {e}")
            else:
                if self.response_log:
                    logger.debug(f'Call API {api_name} SUCCESS: {data}')

        return data
