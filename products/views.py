from django.shortcuts import render
from .models import Product,Collection
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    collections = Collection.objects.all()[:4]
    featured_products = Product.objects.order_by('priority')[:4]
    exclusive = Product.objects.get(priority=10)
    context = {'collections':collections,'featured':featured_products,'exclusive':exclusive}
    return render(request,'index.html',context)

def prdlist(request):
    page = 1
    if request.GET:
        page = request.GET.get('page')
    products = Product.objects.all()
    product_paginator = Paginator(products,12)
    products = product_paginator.get_page(page)
    context = {'products':products}
    return render(request,'productlist.html',context)

def prddes(request,pk):
    product = Product.objects.get(id=pk)
    context = {'product':product}
    return render(request, 'productdes.html',context)

def collection_view(request,collection_name):
    shirts = Product.objects.filter(collection__collection_name=collection_name)
    context = {'products':shirts}
    return render(request,'productlist.html',context)