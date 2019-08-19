from products.models import Product
from api.serializers import ProductSerializer
from rest_framework import viewsets




# YOUR VIEWS HERE
class ProductModelViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

