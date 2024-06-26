from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('products',views.prdlist,name='products'),
    path('productdescription/<pk>',views.prddes,name='productdes'),
    path('collectionview/<str:collection_name>/',views.collection_view,name='collectionview')
]