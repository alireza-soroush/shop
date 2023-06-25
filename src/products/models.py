from django.db import models
from alireza.django_tools import rename_file

class Product(models.Model):
    title = models.CharField('محصول',max_length=20,null=False,blank=False)
    description = models.CharField('توضیحات',max_length=50,null=False,blank=False)
    extra_description = models.TextField('توضیحات اضافه',max_length=400,null=False,blank=False)

    amount = models.PositiveSmallIntegerField('مقدار موجود',null=False,blank=False)
    price = models.PositiveIntegerField('قیمت',null=False,blank=False)
    sales = models.SmallIntegerField('فروش',default=0,editable=False)
    image = models.ImageField('عکس',upload_to=rename_file)

    date = models.DateTimeField('تاریخ',auto_now_add=True)

    class Meta :
        verbose_name = 'محصول'
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.title
    

class ProductComment(models.Model):
    user = models.OneToOneField('account.User',verbose_name='کاربر',on_delete=models.CASCADE)
    forproduct = models.OneToOneField(Product,verbose_name='برای محصول',on_delete=models.CASCADE)
    comment = models.TextField('کامنت',max_length=100)
    date = models.DateTimeField('تاریخ',auto_now_add=True)

    class Meta :
        verbose_name = 'کامنت محصول'
        verbose_name_plural = "کامنت های محصولات"


class ProductCategory(models.Model):
    category_name = models.CharField('نام دسته بندی',max_length=20)
    products = models.ManyToManyField(Product,blank=True,verbose_name='محصولات',)

    class Meta :
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = "دسته بندی های محصولات"

    def __str__(self):
        return self.category_name