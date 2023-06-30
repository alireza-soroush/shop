from django.db import models


class Blog(models.Model):
    title = models.CharField('موضوع',max_length=25,null=False,blank=False)
    description = models.TextField('متن',max_length=5000,null=False,blank=False)
    author = models.CharField('نویسنده',max_length=50)
    image = models.ImageField('عکس',)
    date = models.DateTimeField('تاریخ',auto_now_add=True)

    @property
    def views(self):
        return BlogViews.objects.filter(blog=self).count()
    views.fget.short_description = 'بازدید ها'
    
    @classmethod
    def get_views(self):
        for blog in self.objects.all():
            yield(blog.id,blog.views)
    

    def __str__(self):
        return self.title
    class Meta:
         verbose_name = 'بلاگ'
         verbose_name_plural = "بلاگ"



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