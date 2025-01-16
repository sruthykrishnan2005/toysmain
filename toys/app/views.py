from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
import os
from django.contrib.auth.models import User
from django.conf import settings
from .models import Category, Product




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


    

def shop_home(req):
        products=Product.objects.all()
        categories=Category.objects.all()
    # if 'shop' in req.session:
    #     data=Product.objects.all()
        return render(req,'shop/home.html',{'products':products,'category':categories})
    # else:
    #     return redirect(shop_login)
    
    

def addproduct(req) :
    if 'shop' in req.session:
        if req.method=='POST':
            pid=req.POST['pid']
            name=req.POST['name']
            dis=req.POST['descrip']
            price=req.POST['price']
            off_price=req.POST['off_price']
            stock=req.POST['stock']
            cate=req.POST['category']
            file=req.FILES['img'] 
            cat=Category.objects.get(pk=cate)
            data=Product.objects.create(pid=pid,name=name,dis=dis,offer_price=off_price,price=price,stock=stock,Category=cat,img=file)
            data.save()
            return redirect(shop_home)
        else:
            cate=Category.objects.all()
            return render(req,'shop/addproduct.html',{'cate':cate})
    else:
        return redirect(shop_login) 
    

def edit_product(req,pid):
    if req.method=='POST':
        p_id=req.POST['pid']
        name=req.POST['name']
        descrip=req.POST['descrip']
        price=req.POST['price']
        off_price=req.POST['off_price']
        stock=req.POST['stock']
        file=req.FILES.get('img')
        if file:
            Product.objects.filter(pk=pid).update(pid=p_id,name=name,dis=descrip,price=price,offer_price=off_price,stock=stock)
            data=Product.objects.get(pk=pid)
            data.img=file
            data.save()
        else:
            Product.objects.filter(pk=pid).update(pid=p_id,name=name,dis=descrip,price=price,offer_price=off_price,stock=stock)
            return redirect(shop_home)
    else:
        data=Product.objects.get(pk=pid)
        cate=Category.objects.all()
        return render(req,'shop/edit.html',{'data':data, 'cate':cate})
    

    
def delete_product(req,pid):
    data=Product.objects.get(pk=pid)
    file=data.img.url
    file=file.split('/')[-1]
    os.remove('media/'+file)
    data.delete()
    return redirect(shop_home)



def add_category(req):
    if 'shop' in req.session:
        if req.method=='POST':
            c_name=req.POST['cate_name']
            c_name=c_name.lower()
            try:
                cate=Category.objects.get( name=c_name)
            except:
                data=Category.objects.create( name=c_name)
                data.save()
            return redirect(add_category)
        categories=Category.objects.all()
        return render(req,'shop/cate.html' ,{'cate':categories})
    else:
        return render(req,'shop/cate.html')


def view_bookings(req):
    buy=Buy.objects.all()[::-1]
    return render(req,'shop/view_booking.html',{'buy':buy})




    
def user_home(req):
    if 'user' in req.session:
        data=Product.objects.all()
        return render(req,'user/home.html',{'Product':data})
    else:
        return redirect(shop_login)
    

    


def contact(req):
    return render(req,'user/contact.html')



def about_us(req):
    return render(req,'user/about.html')



def product_view(req,pid):
       data=Product.objects.get(pk=pid)
       return render(req,'user/view_pro.html',{'product':data})



# def category_view(req, category_id):
#     try:
#         category = Category.objects.get(pid=category_id)
#     except Category.DoesNotExist:
#         return render(req, 'user/view_cate.html', {'error': 'Category does not exist'})
    
#     products = Product.objects.filter(category=category)  
#     return render(req, 'user/view_cate.html', {'category': category, 'products': products})


def category_view(request, cid):
    # Get the category or return 404 if not found
    category = get_object_or_404(Category, pk=cid)
    
    # Fetch all products related to this category
    products = Product.objects.filter(category=category)
    
    # Pass the category and products to the template
    return render(request, 'user/view_cate.html', {'category': category, 'products': products})

def qty_in(req,cid):
    data=Cart.objects.get(pk=cid)
    data.qty+=1
    data.save()
    return redirect(view_cart)

def qty_dec(req,cid):
    data=Cart.objects.get(pk=cid)
    data.qty-=1
    data.save()
    print(data.qty)
    if data.qty==0:
        data.delete()
    return redirect(view_cart)





def add_to_cart(req,pid):
    product=Product.objects.get(pk=pid)
    user=User.objects.get(username=req.session['user'])
    try:
        cart=Cart.objects.get(user=user,product=product)
        cart.qty+=1
        cart.save()
    except:
        data=Cart.objects.create(product=product,user=user,qty=1)
        data.save()
    return redirect(view_cart)



def view_cart(req):
    user=User.objects.get(username=req.session['user'])
    data=Cart.objects.filter(user=user)
    return render(req,'user/cart.html',{'cart':data})



def cart_pro_buy(req,cid):
    cart=Cart.objects.get(pk=cid)
    product=cart.product
    user=cart.user
    qty=cart.qty
    price=product.offer_price*qty
    buy=Buy.objects.create(product=product,user=user,qty=qty,price=price)
    buy.save()
    return redirect(bookings)




def pro_buy(req,pid):
    product=Product.objects.get(pk=pid)
    user=User.objects.get(username=req.session['user'])
    qty=1
    price=product.offer_price
    buy=Buy.objects.create(product=product,user=user,qty=qty,price=price)
    buy.save()
    return redirect(bookings)



def bookings(req):
    user=User.objects.get(username=req.session['user'])
    buy=Buy.objects.filter(user=user)[::-1]
    return render(req,'user/bookings.html',{'bookings':buy})


def ride_on_vehicles(request, name):
    try:
        category = Category.objects.get(name)
    except Category.DoesNotExist:
        category = None
    
    return render(request, 'user/ride on vehicles.html', {'category': category})