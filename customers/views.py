from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
import random
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
        username = request.POST.get('username')
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

def otppage(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            email = request.POST.get('username')
            try:
                user = User.objects.get(username=email)
                subject = 'Your otp is'
                recipient = email
                otp = ''.join([str(random.randint(0, 9)) for _ in range(4)])
                customer = Customer.objects.get(user=user)
                customer.otp = otp
                customer.save()
                message = otp
                send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
                messages.success(request,'OTP has been sent')
                context = {'email': email}
                return render(request, 'otpval.html', context)
            except User.DoesNotExist:
                messages.error(request, 'User does not exist/ incorrect mail')
        elif 'register' in request.POST:
            return accountview(request)

    return render(request, 'otp_page.html')
#keso cydc cxfn hmlq

def otpval(request):
    otp = request.GET.get('otp')
    email = request.GET.get('email')
    user = User.objects.get(username=email)
    customer = Customer.objects.get(user=user)
    context={'email':email}
    if customer.otp == otp:
        login(request,user)
        return redirect('home')
    else:
        messages.error(request,'Incorrect OTP')
        return render(request,'otpval.html',context)