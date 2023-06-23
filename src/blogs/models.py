from django.db import models







class Blog(models.Model):
    title = models.CharField('موضوع',max_length=25,null=False,blank=False)
    description = models.TextField('متن',max_length=300,null=False,blank=False)
    author = models.CharField('نویسنده',max_length=50)

    image = models.ImageField('عکس',)

    views = models.PositiveIntegerField('بازدید',default=0,editable=False)

    date = models.DateTimeField('تاریخ',auto_now_add=True)
    
    class Meta:
         verbose_name = 'بلاگ'
         verbose_name_plural = "بلاگ"

class BlogCategory(models.Model):
    category_name = models.CharField('نام دسته بندی',max_length=20)
    blogs = models.ManyToManyField(Blog,blank=True,verbose_name='بلاگ ها')

    class Meta:
         verbose_name = 'دسته بندی بلاگ'
         verbose_name_plural = "دسته بندی های بلاگ"

class BlogComment(models.Model):
    user = models.OneToOneField('account.User',verbose_name='کاربر',on_delete=models.CASCADE)
    for_blog= models.OneToOneField(Blog,verbose_name='برای بلاگ',on_delete=models.CASCADE)
    comment = models.TextField('کامنت',max_length=100)
    date = models.DateTimeField('تاریخ',auto_now_add=True)

    class Meta:
         verbose_name = 'کامنت بلاگ'
         verbose_name_plural = "کامنت های بلاگ"