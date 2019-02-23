from rest_framework import serializers

from products.models import Product, Category
# model comes from product directory

class ProductSerializer(serializers.ModelSerializer):
    # YOUR CODE HERE
    class Meta:
        model = Product
        
        fields = ('id', 'name', 'sku', 'category', 'description', 'price',
                      'created', 'featured',)

# META:
#Model metadata is “anything that’s not a field”, such as ordering options (ordering), database table name (db_table), 
# or human-readable singular and plural names (verbose_name and verbose_name_plural). 
# None are required, and adding class Meta to a model is completely optional.
    
##### Based on class PRODUCT attributes

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     sku = models.CharField(max_length=8)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     description = models.CharField(max_length=1000, blank=True)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     created = models.DateTimeField(auto_now_add=True)
#     featured = models.BooleanField(default=False)

# forgot the inheritance here
'''ZONA: Ah I see a couple issues. Your ProductSerializer isn't inheriting from the ModelSerializer class, so it's just a new class with a couple variables saved to it. Next in your serializer you have the right attributes but they aren't quite set in the right way, I would check the docs on ModelSerializers against what you have. It's a small but important difference in how you're setting it up (if you have a working example of a ModelForm on hand, that would also provide an example of what you're leaving out). (edited) '''