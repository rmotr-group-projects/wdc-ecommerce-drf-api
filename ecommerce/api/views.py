from rest_framework import viewsets

from .serializers import ProductModelSerializer
from products.models import Product, Category, ProductImage


class ProductModelViewSet(viewsets.ModelViewSet):
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()