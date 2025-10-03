import mimetypes
import os
import threading
from typing import Tuple

from django.conf import settings
from django.db.models import Q
from rest_framework.pagination import LimitOffsetPagination

from applications.products.models.product import Product
from applications.products.serializers.product_serializers import ProductDetailSerializer, ProductResponseSerializer
from applications.products.services.exceptions import ProductExistedException, ProductNotExistException
from libs.hashmap import hashmap
from libs.tracing.decorator import pretty_function
from libs.tracing.django_logger import DjangoLogging
from libs.ultils import delete_old_image, delete_attachments_by_product_id


class ProductService:
    @staticmethod
    @pretty_function()
    def create(data, image_url, logger: DjangoLogging = None) -> dict:
        logger.info("In side ProductService")
        data["image_url"] = image_url

        # check product existing
        is_exiting = Product.objects.filter(name=data["name"]).exists()
        if is_exiting:
            raise ProductExistedException(product_name=data["name"])

        # save new record
        product = Product.objects.create(**data)
        return ProductDetailSerializer(product).data

    @staticmethod
    @pretty_function()
    def fetch(limit, offset, data_filters, logger: DjangoLogging = None):
        logger.info("In side ProductService")
        total_items = Product.objects.count()

        # filter
        filters = Q()
        if search := data_filters.get("search"):
            search_filters = Q()
            search_filters |= Q(name__icontains=search)
            search_filters |= Q(description__icontains=search)
            filters &= search_filters

        products = Product.objects.values(
            "id",
            "name",
            "image_url",
            "created_at",
            "updated_at",
        ).filter(filters).distinct()
        for p in products:
            print(p)

        return ProductResponseSerializer(
            products[offset:offset + limit], many=True
        ).data, total_items

    @staticmethod
    @pretty_function()
    def get_detail(product_id, logger: DjangoLogging = None) -> dict:
        logger.info("In side ProductService")
        product = Product.objects.filter(id=product_id).first()
        if not product:
            raise ProductNotExistException()
        result = ProductDetailSerializer(product).data
        result["attachments"] = ProductService.build_tree_folder(product_id)
        return result

    @staticmethod
    def update(product_id, data, new_image=None, logger: DjangoLogging = None) -> dict:
        logger.info("In side ProductService")
        # checking exist
        is_exiting = Product.objects.filter(id=product_id).exists()
        if not is_exiting:
            raise ProductNotExistException()

        if new_image:
            data["image_url"] = new_image

        # update product
        product = Product.objects.filter(id=product_id).first()
        old_image = product.image_url

        thread_delete_old_image = threading.Thread(target=delete_old_image, args=(old_image,))
        for key, value in data.items():
            setattr(product, key, value)
        product.save()

        # delete old image with thread
        if data.get("image_url"):
            thread_delete_old_image.start()

        return ProductDetailSerializer(product).data

    @staticmethod
    def delete(product_id, logger: DjangoLogging = None) -> str:
        logger.info("In side ProductService")
        product = Product.objects.filter(id=product_id).first()
        old_image = product.image_url

        thread_delete_products = threading.Thread(
            target=delete_attachments_by_product_id,
            args=(os.path.join("storage", "products", product_id),)
        )
        thread_delete_old_image = threading.Thread(target=delete_old_image, args=(old_image,))
        thread_delete_item_hashmap = threading.Thread(target=hashmap.delete, args=(product_id,))

        product.delete()

        thread_delete_item_hashmap.start()
        thread_delete_old_image.start()
        thread_delete_products.start()

        return "Success"

    @staticmethod
    @pretty_function()
    def upload(product_id, files, logger):
        logger.info("In side ProductService")
        folder_types = {
            "images": [".png", ".jpg", ".jpeg", ".gif"],
            "icons": [".ico", ".svg"],
            "docs": [".doc", ".docx", ".txt", ".xlsx", ".csv"],
            "media": [".mp4", ".mp3"],
            "pdf": [".pdf"]
        }

        # base folder
        product_folder = os.path.join(settings.MEDIA_ROOT, "products", str(product_id))
        os.makedirs(product_folder, exist_ok=True)

        for f in files:
            filename = getattr(f, "name", str(f))
            ext = os.path.splitext(filename)[1].lower()

            # find folder
            folder_name = None
            for key, exts in folder_types.items():
                if ext in exts:
                    folder_name = key
                    break

            if not folder_name:
                if logger:
                    logger.warning(f"File {filename} không được phân loại")
                continue

            folder_path = os.path.join(product_folder, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            # save file
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "wb") as fw:
                fw.write(f.read())
            mime_type, _ = mimetypes.guess_type(filename)
            hashmap.set(product_id, {
                os.path.join(folder_name, filename): {
                    "size": os.path.getsize(file_path),
                    "type": mime_type
                }
            })
        return ProductService.build_tree_folder(product_id)

    @staticmethod
    def build_tree_folder(product_id):
        path_items = hashmap.get(product_id) or []
        dict_file = dict()

        for path in path_items:
            levels = list(path.keys())[0].split("/")
            ProductService.insert_by_path(
                dict_file,
                levels,
                path[list(path.keys())[0]]
            )

        return {
            "storage": {
                "products": {
                    product_id: dict_file
                }
            }
        }

    @staticmethod
    def insert_by_path(data, path, value):
        current = data
        for key in path[:-1]:
            if key not in current or not isinstance(current[key], dict):
                current[key] = {}
            current = current[key]
        current[path[-1]] = value
        return data
