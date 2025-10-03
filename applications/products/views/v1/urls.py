from django.urls import path

from applications.products.views.v1 import views

urlpatterns = [
    path("create", views.create_product, name="create_product"),
    path("products", views.fetch, name="fetch_products"),
    path("product/<str:product_id>", views.get_detail, name="get_product_detail"),
    path("update/<str:product_id>", views.update, name="update_product"),
    path("delete/<str:product_id>", views.delete, name="delete_product"),
    path("uploads/<str:product_id>", views.upload, name="upload_attachments"),
]
