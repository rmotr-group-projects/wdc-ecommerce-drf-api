from rest_framework import serializers

from products.models import Product, Category
# model comes from product directory

class ProductSerializer():
    # YOUR CODE HERE
    model = Product
    
    fields = ('id', 'name', 'sku', 'category', 'description', 'price',
                  'created', 'featured',)

    
    
##### Based on class PRODUCT attributes

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     sku = models.CharField(max_length=8)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     description = models.CharField(max_length=1000, blank=True)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     created = models.DateTimeField(auto_now_add=True)
#     featured = models.BooleanField(default=False)