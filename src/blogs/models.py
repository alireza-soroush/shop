from django.db import models
from alireza.DjangoTools import rename_file
from slugify import slugify
from alireza.UsefulTools import random_string
def rename_profile_pic(instance,filename):
    return rename_file(instance,filename,hardpath='blogs')

class Blog(models.Model):
    title = models.CharField('موضوع',max_length=25,null=False,blank=False)
    description = models.TextField('متن',max_length=5000,null=False,blank=False)
    author = models.CharField('نویسنده',max_length=50)
    slug = models.SlugField(editable=False,blank=True)
    image = models.ImageField('عکس',upload_to=rename_profile_pic)
    date = models.DateTimeField('تاریخ',auto_now_add=True)

    @property
    def views(self):
        return BlogViews.objects.filter(blog=self).count()
    views.fget.short_description = 'بازدید ها'
    
    @classmethod
    def get_views(cls):
        for blog in cls.objects.all():
            yield(blog.id,blog.views)
    

    def __str__(self):
        return self.title
    class Meta:
         verbose_name = 'بلاگ'
         verbose_name_plural = "بلاگ"

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        if len(self.slug)<1:
            self.slug=random_string(10,True)
        super().save(*args,**kwargs)

class BlogComment(models.Model):
    user = models.ForeignKey('account.User',verbose_name='کاربر',on_delete=models.CASCADE)
    for_blog= models.ForeignKey(Blog,verbose_name='برای بلاگ',on_delete=models.CASCADE)
    comment = models.TextField('کامنت',max_length=200)
    date = models.DateTimeField('تاریخ',auto_now_add=True)

    class Meta:
         verbose_name = 'کامنت بلاگ'
         verbose_name_plural = "کامنت های بلاگ"



class BlogViews(models.Model):
    IPAddres= models.GenericIPAddressField(default='192.168.1.1')
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.title