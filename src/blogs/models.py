from django.db import models







class Blog(models.Model):
    title = models.CharField(max_length=25,null=False,blank=False)
    description = models.TextField(max_length=300,null=False,blank=False)
    author = models.CharField(max_length=50)

    image = models.ImageField()

    views = models.PositiveIntegerField(default=0,editable=False)

    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
         verbose_name_plural = "بلاگ"

class BlogCategory(models.Model):
    category_name = models.CharField(max_length=20)
    category_image = models.ImageField()
    blogs = models.ManyToManyField(Blog)

    class Meta:
         verbose_name_plural = "دسته بندی های بلاگ"

class BlogComment(models.Model):
    user = models.OneToOneField('account.User',on_delete=models.CASCADE)
    for_blog= models.OneToOneField(Blog,on_delete=models.CASCADE)
    comment = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
         verbose_name_plural = "کامنت های بلاگ"