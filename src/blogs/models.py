from django.db import models
from django.contrib.auth.models import User







class Blog(models.Model):
    title = models.CharField(max_length=25,null=False,blank=False)
    description = models.TextField(max_length=300,null=False,blank=False)
    author = models.CharField(max_length=50)

    image = models.ImageField()

    views = models.PositiveIntegerField(default=0,editable=False)

    date = models.DateTimeField(auto_now_add=True)

class BlogCategory(models.Model):
    category_name = models.CharField(max_length=20)
    category_image = models.ImageField()
    blogs = models.ManyToManyField(Blog)


class BlogComment(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    for_blog= models.OneToOneField(Blog,on_delete=models.CASCADE)
    comment = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
