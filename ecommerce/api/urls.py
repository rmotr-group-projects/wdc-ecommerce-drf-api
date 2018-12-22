from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()

# Register the 'products' urls in the router
router.register('...')

urlpatterns = []
urlpatterns += router.urls
