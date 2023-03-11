from rest_framework import serializers
from .models import ProductsProducts

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsProducts
        fields = '__all__'
