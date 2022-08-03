from django.urls import path
from .views import *

urlpatterns = [
    path('', get_brands, name='get_brands'),
    path('model/<int:madel_id>', get_models, name='get_models'),
    path('product/<int:product_id>', get_products, name='get_products'),
]