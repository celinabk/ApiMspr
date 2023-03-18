from rest_framework import serializers
from .models import ProductsProducts, Order, OrderItem, Customer

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsProducts
        fields = '__all__'
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'