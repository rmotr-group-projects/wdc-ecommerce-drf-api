from products.models import Product
from api.serializers import ProductSerializer
from rest_framework import viewsets


# YOUR VIEWS HERE
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer