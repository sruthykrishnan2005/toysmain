from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
import os
from django.contrib.auth.models import User



# Create your views here.
def shop_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    if 'user' in req.session:
        return redirect(user_home)
    if req.method=='POST':
        Username=req.POST['username']
        Password=req.POST['password']
        data=authenticate(username=Username,password=Password)
        if data:
            login(req,data)
            if data.is_superuser:
                req.session['shop']=Username
                return redirect(shop_home)
            else:
                req.session['user']=Username
                return redirect(user_home)
        else:
            messages.warning(req, "invalid password")
            return redirect(shop_login)
    else:
        return render(req,'login.html')

def shop_logout(req):
    logout(req)
    req.session.flush()
    return redirect(shop_login)
    

def shop_home(req):
    if 'shop' in req.session:
        data=Product.objects.all()
        return render(req,'shop/home.html',{'products':data})
    else:
        return redirect(shop_login)
    
    
def register(req):
    if req.method=='POST':
        uname=req.POST['uname']
        email=req.POST['email']
        password=req.POST['password']
        try:
            data=User.objects.create_user(first_name=uname,email=email,username=email,password=password)
            data.save()
        except:
            messages.warning(req,"email alreadyin use")
            return redirect(register)
        return redirect(shop_login)
    else:
        return render(req,'user/register.html')
    

    
    
def user_home(req):
    if 'user' in req.session:
        data=Product.objects.all()
        return render(req,'user/home.html',{'products':data})
    else:
        return redirect(shop_login)