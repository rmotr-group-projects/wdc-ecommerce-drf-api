from rest_framework import serializers

from products.models import Product, Category


class ProductModelSerializer(serializers.ModelSerializer):
    # YOUR CODE HERE
    class Meta:
        model = Product
        fields = ('id','name','sku','category','description','price','created','featured')
        
