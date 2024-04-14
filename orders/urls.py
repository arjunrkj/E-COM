from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('cart', views.cart, name='cart'),
    path('addtocart',views.addtocart, name='addtocart'),
    path('removeitem/<pk>',views.removeitem, name='removeitem'),
    path('orderpage',views.orderpage, name='orderpage'),
    path('orderconfirm',views.orderconfirm, name='orderconfirm')
]