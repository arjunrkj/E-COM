from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('account', views.accountview, name='account'),
    path('logout',views.sign_out,name='logout'),
    path('otppage',views.otppage,name='otppage'),
    path('otpval',views.otpval,name='otpval')
]