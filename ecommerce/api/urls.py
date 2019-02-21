from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()

router.register('products', views.ProductViewSet, base_name='products')  # 'products' first argument is path('products/', ...)... New urls are generated off this
                                                # base_name='product' is like name='product' in a path()

urlpatterns = [url for url in router.urls]

# OR do the following from an empty list:
# urlpatterns += router.urls
