from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request,'index.html')

def prdlist(request):
    products = Product.objects.all()
    product_paginator = Paginator(products,12)
    products = product_paginator.get_page(1)
    context = {'products':products}
    return render(request,'productlist.html',context)

def prddes(request):
    return render(request, 'productdes.html')