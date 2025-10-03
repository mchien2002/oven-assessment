import base64
import hashlib

import jwt
from django.conf import settings

from libs.exceptions.authentication import UnauthenticatedClient
from libs.exceptions.commons import ExpiredTokenException


class ClientAuthentication:

    @classmethod
    def get_hexdigits(cls, _string: str):
        return hashlib.md5(_string.encode()).hexdigest()

    @classmethod
    def authentication(cls, authentication_key):
        try:
            payload = jwt.decode(
                authentication_key,
                settings.SECRET_KEY,
                algorithms=["HS256"],
            )
            return payload
        except jwt.ExpiredSignatureError:
            raise ExpiredTokenException()
        except jwt.InvalidTokenError as e:
            raise UnauthenticatedClient()

    @classmethod
    def make_authentication(cls, client_id, password):
        id_pass = f'{client_id}:{hashlib.md5(password.encode()).hexdigest()}'
        return base64.b64encode(id_pass.encode("ascii")).decode("ascii")

    @classmethod
    def load_service_authentication(cls):
        if hasattr(settings, "SERVICE_AUTHENTICATION") and isinstance(settings.SERVICE_AUTHENTICATION, dict):
            for service_name, data in settings.SERVICE_AUTHENTICATION.items():
                setattr(cls, service_name, {
                    "protocol": data["protocol"],
                    "host_name": data["host"],
                    "headers": {
                        "Authorization": f'Basic {cls.make_authentication(data["client_id"], data["client_password"])}',
                        "User-Agent": "workspace-admin"
                    }
                })


ClientAuthentication.load_service_authentication()
