from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    pid=models.TextField()
    name=models.TextField()
    dis=models.TextField()
    price=models.IntegerField()
    offer_price=models.IntegerField()
    stock=models.IntegerField()
    img=models.FileField()
    

class Buy(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    qty=models.IntegerField()
    price=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    
class Contact(models.Model):
    name = models.TextField()
    phone_number = models.TextField() 
    email = models.EmailField()