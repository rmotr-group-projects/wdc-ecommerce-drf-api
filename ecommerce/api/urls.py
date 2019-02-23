from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()

# Register the 'products' urls in the router
#router.register('...')
router.register('products', views.ProductViewSet, base_name='products')


# How should I know how to setup the URLs?

urlpatterns = []
urlpatterns += router.urls

