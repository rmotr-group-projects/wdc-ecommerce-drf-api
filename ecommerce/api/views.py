from rest_framework import viewsets
from products.models import Product
from api.serializers import ProductModelSerializer


class ProductViewSet(viewsets.ModelViewSet):  # No need to make .put(), .post() etc due to this ModelViewSet
    serializer_class = ProductModelSerializer  # Make serializer to turn a Model into a JSON object...
    queryset = Product.objects.all()  # DRF knows to .get() a detail view, etc... Do .all() as standard
                                      # But, you can .filter() this etc.
