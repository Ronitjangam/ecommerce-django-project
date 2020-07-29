from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cataegory(models.Model):
    cname=models.CharField(max_length=30)
    def __str__(c):
        return c.cname
    

class Product(models.Model):
    pname=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=200)
    pimage=models.ImageField(upload_to="media",default="")
    category=models.ForeignKey(Cataegory,on_delete=models.CASCADE)
    def __str__(c):
        return c.pname


class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


class Order(models.Model):
    totalbill=models.IntegerField()
    orderdate=models.DateField(auto_now=True)
    status=models.CharField(max_length=30,default="processing")
    user=models.ForeignKey(User,on_delete=models.CASCADE)

        
        
class MyImage(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=300)
    img=models.ImageField(upload_to="media",default="")