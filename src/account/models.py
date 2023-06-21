from django.db import models
from django.contrib.auth.models import User



class Account(models.Model):
    user = models.OneToOneField(User,null=False,blank=False,on_delete=models.CASCADE)
    
    company = models.CharField(max_length=25,null=True,blank=True)
    area = models.CharField(max_length=25,null=True,blank=True)

    state= models.CharField(max_length=30,null=False,blank=False,)
    city= models.CharField(max_length=30,null=False,blank=False,)
    street = models.CharField(max_length=80,null=False,blank=False)
    house_plate = models.PositiveSmallIntegerField(null=False,blank=False)
    zipcode = models.IntegerField(null=False,blank=False)
    phone = models.IntegerField(null=False,blank=False)
    cart = models.ManyToManyField(to='products.Product',null=True,blank=True)