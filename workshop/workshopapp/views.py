from django.shortcuts import render
from rest_framework.response import Response

from .models import ProductsProducts, Order, OrderItem, Customer
from .serializers import ProductsSerializer, OrderSerializer, OrderItemSerializer, CustomerSerializer
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


class CustomerViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/products  get request
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)

    def create(self, request):  # /api/products  put requets
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):  # /api/products/<str:id>
        customer = Customer.objects.get(id=pk)
        serializer = CustomerSerializer(customer)

        return Response(serializer.data)

    def update(self, request, pk=None):  # /api/products/<str:id>
        customer = Customer.objects.get(id=pk)
        serializer = CustomerSerializer(instance=customer,data=request.data)  # update intance data to data get from request
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):  # /api/products/<str:id>
        customer = Customer.objects.get(id=pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/products  get request
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def create(self, request):  # /api/products  put requets
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):  # /api/products/<str:id>
        order = Order.objects.get(id=pk)
        serializer = OrderSerializer(order)
        print(serializer, "++++++++++++++++++++++++++")
        return Response(serializer.data)

    def update(self, request, pk=None):  # /api/products/<str:id>
        order = Order.objects.get(id=pk)
        serializer = ProductsSerializer(instance=order,
                                        data=request.data)  # update intance data to data get from request
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):  # /api/products/<str:id>
        order = Order.objects.get(id=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderItemViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/products  get request
        orderItem = OrderItem.objects.all()
        serializer = OrderItemSerializer(orderItem, many=True)
        return Response(serializer.data)

    def create(self, request):  # /api/products  put requets
        serializer = OrderItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
