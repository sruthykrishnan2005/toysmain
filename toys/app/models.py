from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name=models.TextField()
    description = models.TextField()

class Product(models.Model):
    pid=models.TextField()
    name=models.TextField()
    dis=models.TextField()
    price=models.IntegerField()
    offer_price=models.IntegerField()
    stock=models.IntegerField()
    img=models.FileField()
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)

    

    
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    qty=models.IntegerField()
    is_active =models.BooleanField(default=True)


class Buy(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    qty=models.IntegerField()
    price=models.IntegerField()
    date=models.DateField(auto_now_add=True)


class Address(models.Model):
    name = models.CharField(max_length=255)  
    city = models.CharField(max_length=100)  
    pin_code = models.CharField(max_length=20) 


    def __str__(self):
        return f"{self.name}, {self.city}, {self.pin_code}"

