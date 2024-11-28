from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
import os


# Create your views here.
def shop_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
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