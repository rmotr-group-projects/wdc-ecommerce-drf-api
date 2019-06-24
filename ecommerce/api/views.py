from rest_framework import viewsets
from products.models import Product
from api.serializers import ProductSerializer


# YOUR VIEWS HERE

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
