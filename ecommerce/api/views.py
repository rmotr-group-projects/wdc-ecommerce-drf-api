import json

from products.models import Product
from api.serializers import ProductModelSerializer

from rest_framework import viewsets


# YOUR VIEWS HERE
class ProductModelViewSet(viewsets.ModelViewSet):
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()