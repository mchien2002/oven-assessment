from rest_framework import status
from rest_framework.exceptions import APIException

from libs.exceptions.commons import APIWarningException


class ProductExistedException(APIWarningException):
    def __init__(self, product_name: str):
        super().__init__(
            message=f"Product with name {product_name} is existed",
            status_code=1500,
            error={
                "name": product_name
            }
        )


class ProductNotExistException(APIWarningException):
    def __init__(self):
        super().__init__(
            message=f"Product not exist",
            status_code=1600,
            error={}
        )
