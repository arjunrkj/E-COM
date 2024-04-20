from django.shortcuts import render,redirect
from .models import Order,OrderItem
from products.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='account')
def cart(request):
    user = request.user
    customer = user.customer_info
    cart_obj,created = Order.objects.get_or_create(owner=customer,order_status=Order.CART_STAGE)
    flag=True
    if cart_obj.added_items.count() == 0:
        flag = False
        messages.error(request,'Your Cart is Empty')
    context = {'cart':cart_obj,'flag':flag}
    return render(request, 'cart.html',context)

@login_required(login_url='account')
def addtocart(request):
    if request.POST:
        user = request.user
        customer = user.customer_info
        quantity = request.POST.get('quantity')
        size = request.POST.get('size')
        product_id = request.POST.get('id')
        cart_obj,created = Order.objects.get_or_create(owner=customer,order_status=Order.CART_STAGE)
        product=Product.objects.get(id=product_id)
        orderitem = OrderItem.objects.create(product=product,owner=cart_obj,quantity=quantity,size=size)
        return redirect('cart')
    
@login_required(login_url='account')
def removeitem(request,pk):
    item=OrderItem.objects.get(id=pk)
    item.delete()
    return redirect('cart')

@login_required(login_url='account')
def orderpage(request):
    mobile = request.user.customer_info.phone
    payable = request.GET.get('total')
    user = request.user
    customer = user.customer_info
    context = {'mobile':mobile,'amount':payable}
    return render(request,'orderpage.html',context)

@login_required(login_url='account')
def orderconfirm(request):
    try:
        if request.POST:
            user = request.user
            customer = user.customer_info
            order_obj = Order.objects.get(owner=customer, order_status=Order.CART_STAGE)
            order_obj.order_status = Order.ORDER_CONFIRMED
            price = float(request.POST.get('amt'))
            order_obj.total_price=price
            order_obj.save()
            messages.success(request, 'Your Order is being Processed')
            messages.success(request, 'You will receive a confirmation message on WhatsApp within 4 hours')
            return render(request, 'confirmorder.html')
    except Exception as e:
        messages.error(request, 'No more items in the cart')
    return render(request,'confirmorder.html')

@login_required(login_url='account')
def view_orders(request):
    user = request.user
    customer = user.customer_info
    all_orders = Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
    context={'orders':all_orders}
    return render(request, 'orderstatus.html',context)