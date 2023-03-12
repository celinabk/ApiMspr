from django.contrib import admin
from django.urls import path

from .views import  ProductsViewSet, RevendeursViewSet#, OrderViewSet

urlpatterns = [
   path('products/', ProductsViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<str:pk>', ProductsViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'put':'destroy'
    })),
    path('revendeurs/',RevendeursViewSet.as_view({
            'get': 'list',
            'post': 'create'
        })),
    path('revendeurs/<str:pk>', RevendeursViewSet.as_view({
                'get': 'retrieve',
                'put': 'update',
                'put':'destroy'
            }))
]