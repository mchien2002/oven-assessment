import unittest
from unittest.mock import patch, MagicMock
from django.db import IntegrityError

from applications.products.services.product_service import ProductService
from libs.tracing.django_logger import DjangoLogging


class TestProductUseCase(unittest.TestCase):
    def setUp(self):
        self.logger = DjangoLogging()

    @patch('applications.products.models.product.Product.objects')
    def test_fetch_products_simple(self, mock_objects):
        mock_objects.count.return_value = 3

        # mock filter() chain: trả luôn danh sách sản phẩm
        mock_objects.values.return_value.filter.return_value.distinct.return_value = [
            {"id": 1, "name": "Laptop Dell XPS 13", "image_url": "dell.jpg"},
            {"id": 2, "name": "Chuột Logitech MX Master 3", "image_url": "mouse.jpg"},
            {"id": 3, "name": "Tai nghe Sony WH-1000XM5", "image_url": "sony.jpg"},
        ]

        products, total_items = ProductService.fetch(limit=30, offset=0, data_filters={}, logger=self.logger)
        self.assertEqual(total_items, len(products))
        self.assertEqual(products[0]["name"], "Laptop Dell XPS 13")



if __name__ == '__main__':
    unittest.main()
