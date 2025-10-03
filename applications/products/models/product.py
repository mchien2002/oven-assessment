import threading

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q

from libs.base_models import BaseModel
from libs.ultils import delete_old_image


class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField(
        validators=[MinValueValidator(1000)]
    )
    image_url = models.ImageField(upload_to="images/", blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    class Router:
        db_name = "db"

    def __str__(self):
        return self.name
