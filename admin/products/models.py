from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
"""class Products(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)
    stock = models.CharField(max_length=50)
    id = models.PositiveIntegerField(default=0, primary_key=True)"""
class Revendeurs(models.Model):
    id = models.PositiveIntegerField( primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    email = models.EmailField()
    mot_de_passe = models.CharField(max_length=128)

    def set_mot_de_passe(self, mot_de_passe):
        self.mot_de_passe = make_password(mot_de_passe)

    def __str__(self):
        return str(self.id)

class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    #price = models.DecimalField(max_digits=10, decimal_places=2)
    creator = models.ForeignKey(Revendeurs, on_delete=models.CASCADE, related_name='products')
    #stock = models.CharField(max_length=50)
    id = models.PositiveIntegerField(default=0, primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)



"""class Order(models.Model):
    customer = models.ForeignKey(Revendeurs, on_delete=models.CASCADE)
    items = models.ManyToManyField(Products, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Stock(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE)"""
