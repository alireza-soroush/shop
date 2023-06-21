from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=20,null=False,blank=False)
    description = models.CharField(max_length=50,null=False,blank=False)
    extra_description = models.TextField(max_length=400,null=False,blank=False)

    amounth = models.PositiveSmallIntegerField(null=False,blank=False)
    price = models.PositiveIntegerField(null=False,blank=False)

    image = models.ImageField()

    date = models.DateTimeField(auto_now_add=True)


class ProductComment(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    forproduct = models.OneToOneField(Product,on_delete=models.CASCADE)
    comment = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

class ProductCategory(models.Model):
    category_name = models.CharField(max_length=20)
    category_image = models.ImageField()
    products = models.ManyToManyField(Product)