from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Order, OrderItem, Category

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.filter(stock__gt=0)
        data = [{
            "id": p.id,
            "title": p.title,
            "price": str(p.price),
            "vendor": p.vendor.store_name,
            "description": p.description
        } for p in products]
        return Response(data)

class CreateOrderView(APIView):
    def post(self, request):
        # Initial minimal implementation structure for basket processing
        data = request.data
        return Response({"message": "Order endpoint baseline setup intact.", "data": data}, status=status.HTTP_201_CREATED)