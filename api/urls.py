from django.urls import path
from api.v1.product.views import ProductView


urlpatterns = [
    path('product/', ProductView.as_view(), name='api_product_list'),
    path('product/<int:pk>/', ProductView.as_view(), name='api_product_one'),
]


