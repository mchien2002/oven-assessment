from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import parser_classes
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.parsers import MultiPartParser

from applications.products.serializers.product_serializers import ProductCreateSerializer, ProductDetailSerializer, \
    ProductResponseSerializer, ProductUpdateSerializer
from applications.products.services.product_service import ProductService
from libs.responses import APIResponse, PaginatorResponse
from libs.tracing.decorator import pretty_api
from libs.tracing.django_logger import DjangoLogging


@swagger_auto_schema(
    method="POST",
    tags=["Products"],
    security=[],
    operation_summary="Create new product",
    manual_parameters=[
        openapi.Parameter(
            name="image_url",
            in_=openapi.IN_FORM,
            type=openapi.TYPE_FILE,
            required=True,
            description="Image Product"
        ),
    ],
    request_body=ProductCreateSerializer,
    responses={
        200: openapi.Response(
            description="Product created",
            schema=ProductDetailSerializer,
        ),
    }
)
@pretty_api(http_methods=["POST"], serializer=ProductCreateSerializer)
@parser_classes([MultiPartParser])
def create_product(request, data_serialized, _response: APIResponse, logger: DjangoLogging, **kwargs):
    logger.debug("In side view")
    files = request.FILES.get("image_url")
    product = ProductService.create(data_serialized, files, logger=logger)
    _response.data_resp = product


@swagger_auto_schema(
    method="GET",
    tags=["Products"],
    security=[],
    operation_summary="Fetch list of product",
    manual_parameters=[
        openapi.Parameter(
            name="offset",
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            required=False
        ),
        openapi.Parameter(
            name="limit",
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            required=False
        ),
        openapi.Parameter(
            name="search",
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            required=False
        ),
    ],
    responses={
        200: openapi.Response(
            description="Product Response",
            schema=ProductResponseSerializer,
        ),
    }
)
@pretty_api(http_methods=["GET"], class_response=PaginatorResponse)
def fetch(request, _response: APIResponse, logger: DjangoLogging, **kwargs):
    logger.debug("In side view")
    paginator = LimitOffsetPagination()
    limit = paginator.get_limit(request)
    offset = paginator.get_offset(request)
    serializer_products, total_items = ProductService.fetch(
        limit,
        offset,
        request.query_params,
        logger=logger)
    _response.data_resp = serializer_products
    _response.count = total_items
    _response.offset = offset
    _response.limit = limit


@swagger_auto_schema(
    method="GET",
    tags=["Products"],
    security=[],
    operation_summary="Get detail product",
    responses={
        200: openapi.Response(
            description="Product Detail",
            schema=ProductDetailSerializer,
        ),
    }
)
@pretty_api(http_methods=["GET"])
def get_detail(request, product_id, _response: APIResponse, logger: DjangoLogging, **kwargs):
    logger.debug("In side view")
    _response.data_resp = ProductService.get_detail(product_id, logger=logger)


@swagger_auto_schema(
    method="PUT",
    tags=["Products"],
    security=[],
    operation_summary="Edit product",
    request_body=ProductUpdateSerializer,
    manual_parameters=[
        openapi.Parameter(
            name="image_url",
            in_=openapi.IN_FORM,
            type=openapi.TYPE_FILE,
            required=False,
            description="Image Product"
        ),
    ],
    responses={
        200: openapi.Response(
            description="Product Detail",
            schema=ProductDetailSerializer,
        ),
    }
)
@pretty_api(http_methods=["PUT"], serializer=ProductUpdateSerializer)
@parser_classes([MultiPartParser])
def update(request, product_id, data_serialized, _response: APIResponse, logger: DjangoLogging, **kwargs):
    logger.debug("In side view")
    new_image = request.FILES.get("image_url", None)
    _response.data_resp = ProductService.update(product_id, data_serialized, new_image, logger=logger)


@swagger_auto_schema(
    method="DELETE",
    tags=["Products"],
    security=[],
    operation_summary="Delete product",
)
@pretty_api(http_methods=["DELETE"])
def delete(request, product_id, _response: APIResponse, logger: DjangoLogging, **kwargs):
    logger.debug("In side view")
    _response.data_resp = ProductService.delete(product_id, logger=logger)


@swagger_auto_schema(
    method="POST",
    tags=["Products"],
    security=[],
    manual_parameters=[
        openapi.Parameter(
            name="files",
            in_=openapi.IN_FORM,
            type=openapi.TYPE_ARRAY,
            items=openapi.Items(type=openapi.TYPE_FILE),
            required=True,
            description="Attachment Product"
        ),
    ],
    operation_summary="Upload attachment product",
)
@pretty_api(http_methods=["POST"])
@parser_classes([MultiPartParser])
def upload(request, product_id, _response: APIResponse, logger: DjangoLogging, **kwargs):
    logger.debug("In side view")
    files = request.FILES.getlist("files")
    _response.data_resp = ProductService.upload(product_id, files, logger=logger)

