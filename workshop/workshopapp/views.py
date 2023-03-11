from django.shortcuts import render
from rest_framework.response import Response

from .models import ProductsProducts
from .serializers import ProductsSerializer
from rest_framework import viewsets
from rest_framework import status


# Create your views here.
class ProductsViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/products  get request
        products = ProductsProducts.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)
    def create(self, request):  # /api/products  put requets
        serializer = ProductsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)