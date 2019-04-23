from products.models import Product
from api.serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets



class ProductAPIView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all() 
