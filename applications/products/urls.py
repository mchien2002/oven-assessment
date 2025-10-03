
from django.urls import include, path

urlpatterns = [
    path('v1/', include('applications.products.views.v1.urls')),
]