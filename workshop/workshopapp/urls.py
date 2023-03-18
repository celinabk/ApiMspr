from django.urls import path
from .views import ProductsViewSet, CustomerViewSet, OrderViewSet, OrderItemViewSet

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
    path('customers/', CustomerViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('customers/<str:pk>', CustomerViewSet.as_view({
                'get': 'retrieve',
                'put': 'update',
                'put':'destroy'
        })),
    path('orders/', OrderViewSet.as_view({
            'get': 'list',
            'post': 'create'
        })),
    path('orders/<str:pk>', OrderViewSet.as_view({
                'get': 'retrieve',
                'put': 'update',
                'put':'destroy'
        })),


]