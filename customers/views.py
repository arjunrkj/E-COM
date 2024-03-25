from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def accountview(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            username = request.POST.get('email')
            password = request.POST.get('password')
            address = request.POST.get('address')
            fullname = request.POST.get('fname')
            number = request.POST.get('phone')
            
            #user creation
            
            user = User.objects.create_user(username=username,password=password)
            

            #customer creation
            Customer.objects.create(
                user=user,
                phone=number,
                address=address,
                name=fullname
            )

            messages.success(request,'Registration Succesful')
            return redirect('home')
        except Exception as e:
            error_msg="email already registered"
            messages.error(request,error_msg)
    
    if request.POST and 'login' in request.POST:
        context['login']=True
        username = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,'Login succesful')
            return redirect('home')
        else:
            # Check if the email exists in the database
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Incorrect password')
            else:
                messages.error(request, 'Email does not exist')



    return render(request, 'account.html',context)

def sign_out(request):
    logout(request)
    return redirect('home')
