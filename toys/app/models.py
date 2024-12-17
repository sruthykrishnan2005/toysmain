from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name=models.TextField()

class Product(models.Model):
    pid=models.TextField()
    name=models.TextField()
    dis=models.TextField()
    price=models.IntegerField()
    offer_price=models.IntegerField()
    stock=models.IntegerField()
    img=models.FileField()
    Category=models.CharField(max_length=100,null=True,blank=True)
    rideonvehicles=models.TextField(null=True,blank=True)
    building=models.TextField(null=True, blank=True)
    dolls=models.TextField(null=True, blank=True)
    img=models.FileField()
    

    
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    qty=models.IntegerField()


class Buy(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    qty=models.IntegerField()
    price=models.IntegerField()
    date=models.DateField(auto_now_add=True)



