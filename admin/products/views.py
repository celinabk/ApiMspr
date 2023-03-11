from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Products, Revendeurs#, Order, OrderItem#, Stock
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .serializers import ProductsSerializer, RevendeursSerializer#, OrderSerializer, OrderItemSerializer#, StockSerializer
from django.db import IntegrityError
from django.core.mail import send_mail
from django.conf import settings

MAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'biranesamb9@gmail.com'
EMAIL_HOST_PASSWORD = 'rlctoytxpdztdkkc'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


class ProductsViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/products  get request
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):  # /api/products  put requets
        serializer = ProductsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):  # /api/products/<str:id>
        product = Products.objects.get(id=pk)
        serializer = ProductsSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):  # /api/products/<str:id>
        product = Products.objects.get(id=pk)
        serializer = ProductsSerializer(instance=product,
                                        data=request.data)  # update intance data to data get from request
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):  # /api/products/<str:id>
        product = Products.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RevendeursViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/products  get request
        revendeurs = Revendeurs.objects.all()
        serializer = RevendeursSerializer(revendeurs, many=True)
        return Response(serializer.data)

    def create(self, request):  # /api/products  put requets
        serializer = RevendeursSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = serializer
        send = False
        try:
            superuser = User.objects.create_superuser(
                username=user.data['username'],
                email=user.data['email'],
                password=user.data['mot_de_passe'])
            superuser.save()
            send = True

            print(" User is created --------------")
        except IntegrityError:
            print(f"Super User with id {user.data['id']} is already present")
        except Exception as e:
            print(e)

        if send == True:
            message = "Test"
            subject = 'Qrcode'
            send_mail(subject, message, settings.EMAIL_HOST_USER, [
                settings.EMAIL_HOST_USER, 'biranebs96@gmail.com', user.data['email']])
            print("THat is Good +++++++++++++++++++++++++")

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):  # /api/products/<str:id>
        revendeurs = Revendeurs.objects.get(id=pk)
        serializer = RevendeursSerializer(revendeurs)
        return Response(serializer.data)

    def update(self, request, pk=None):  # /api/products/<str:id>
        revendeurs = Revendeurs.objects.get(id=pk)
        serializer = RevendeursSerializer(instance=revendeurs,data=request.data)  # update intance data to data get from request
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):  # /api/products/<str:id>
        revendeur = Revendeurs.objects.get(id=pk)
        revendeur.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""class OrderViewSet(viewsets.ViewSet):
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

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):  # /api/products/<str:id>
        orderItem = OrderItem.objects.get(id=pk)
        serializer = OrderSerializer(orderItem)
        return Response(serializer.data)

    def update(self, request, pk=None):  # /api/products/<str:id>
        orderItem = OrderItem.objects.get(id=pk)
        serializer = ProductsSerializer(instance=orderItem,
                                        data=request.data)  # update intance data to data get from request
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):  # /api/products/<str:id>
        orderItem = OrderItem.objects.get(id=pk)
        orderItem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class StockViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/products  get request
        stock = Stock.objects.all()
        serializer = StockSerializer(stock, many=True)
        return Response(serializer.data)

    def create(self, request):  # /api/products  put requets
        serializer = StockSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):  # /api/products/<str:id>
        stock = Stock.objects.get(id=pk)
        serializer = StockSerializer(stock)
        return Response(serializer.data)

    def update(self, request, pk=None):  # /api/products/<str:id>
        stock = Stock.objects.get(id=pk)
        serializer = ProductsSerializer(instance=stock,
                                        data=request.data)  # update intance data to data get from request
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):  # /api/products/<str:id>
        stock = Stock.objects.get(id=pk)
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)"""

