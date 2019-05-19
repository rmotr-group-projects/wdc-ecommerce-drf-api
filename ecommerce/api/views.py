from products.models import Product
from api.serializers import ProductSerializer
import json

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

# from api.models import People, Planet
# from api.serializers import PeopleSerializer, PeopleModelSerializer

# YOUR VIEWS HERE
class ProductModelViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()