from django.urls import path
from .views import ProductListView, CreateOrderView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('orders/create/', CreateOrderView.as_view(), name='create_order'),
]