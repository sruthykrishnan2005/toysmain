from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
import os
from django.contrib.auth.models import User
from .models import Contact



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
    

def addproduct(req):
    if 'shop' in req.session:
        if req.method=='POST':
            pid=req.POST['pid']
            name=req.POST['name']
            descrip=req.POST['descrip']
            price=req.POST['price']
            off_price=req.POST['off_price']
            stock=req.POST['stock']
            file=req.FILES['img']
            data=Product.objects.create(pid=pid,name=name,dis=descrip,price=price,offer_price=off_price,stock=stock,img=file)
            data.save()
            return redirect(shop_home)
        else:
            return render(req,'shop/addproduct.html')
    else:
        return redirect(shop_login)
    
def delete_product(req,pid):
    data=Product.objects.get(pk=pid)
    file=data.img.url
    file=file.split('/')[-1]
    os.remove('media/'+file)
    data.delete()
    return redirect(shop_home)


def view_bookings(req):
    buy=Buy.objects.all()[::-1]
    return render(req,'shop/view_booking.html',{'buy':buy})

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        phno=request.POST.get('phno')
        email=request.POST.get('email')
        # if name and phno and email:
        data=Contact.objects.create(name=name,phone_number=phno,email=email)
        data.save()
        
    return render(request,'contact.html')



