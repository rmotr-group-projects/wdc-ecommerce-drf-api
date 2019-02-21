from rest_framework import serializers
from products.models import Product


class ProductModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product  # model to serialize into JSON
        fields = ['id', 'name', 'sku', 'category', 'description', 'price', 'created', 'featured']  # can be tuple
