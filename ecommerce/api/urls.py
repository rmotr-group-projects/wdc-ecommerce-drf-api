from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()
router.register('products', views.ProductModelViewSet, base_name='products')
# Register the 'products' urls in the router


urlpatterns = []
urlpatterns += router.urls
