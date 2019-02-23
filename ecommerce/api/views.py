from products.models import Product
from api.serializers import ProductSerializer

from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
    
    # attribute of this class, where is it used again?
    serializer_class = ProductSerializer   #this is a class we make up under api/serializers.py
    
    # retrieve all objects from a table
    queryset = Product.objects.all()
    
# 1. Did the views.py stuff based on notes from class
# 2. Ran tests, got error viewsets not defined
# 3. Included viewsets from class notes and looking online
# 4. Ran tests again, all failed
# 5. Looks like I need to create a product in the database and get back that JSON response? Make serializer?
# 6. Created the serializer.
# 7. Ran tests again, looks like I need the URLs to send requests to.
# 8. Created the URL router, had to look at solution.
# 9. Ran tests again, I think I'm not failing "test_delete" but failing everything else.


# EXPLAINED: Rather than writing your own viewsets, you'll often want to use the existing base classes that provide a default set of behavior.
# There are two main advantages of using a ViewSet class over using a View class.

#Repeated logic can be combined into a single class.
# By using routers, we no longer need to deal with wiring up the URL conf ourselves.
# Both of these come with a trade-off. Using regular views and URL confs is more explicit and gives you more control.
# ViewSets are helpful if you want to get up and running quickly, or when you have a large API and you want to enforce a consistent URL configuration throughout.
    
# YOUR VIEWS HERE

# GET /api/products/ # LIST
# GET /api/products/<product_id> # DETAIL
# POST /api/products/ # CREATE
# PUT /api/products/<product_id> # FULL update
# PATCH /api/products/<product_id> # partial update
# DELETE /api/products/<product_id>



# QUESTIONS:
# Explain routers

# Router note: REST framework adds support for automatic URL routing to Django, and provides you with a simple, quick and consistent way of wiring your view logic to a set of URLs.

# DID NOT HAVE VIEWSET, included it 

#ViewSets
#After routing has determined which controller to use for a request, your controller is responsible for making sense of the request and producing the appropriate output.

#— Ruby on Rails Documentation

#Django REST framework allows you to combine the logic for a set of related views in a single class, called a ViewSet. In other frameworks you may also find conceptually similar implementations named something like 'Resources' or 'Controllers'.

#A ViewSet class is simply a type of class-based View, that does not provide any method handlers such as .get() or .post(), and instead provides actions such as .list() and .create().