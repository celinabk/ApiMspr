from rest_framework import serializers
from .models import Products, Revendeurs#, Order, OrderItem, Stock


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class RevendeursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revendeurs
        fields = '__all__'


"""class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__' """