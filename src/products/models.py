from django.db import models
from alireza.DjangoTools import rename_file
from alireza.UsefulTools import random_string
from slugify import slugify

def rename_profile_pic(instance,filename):
    return rename_file(instance,filename,hardpath='products')
class Product(models.Model):
    title = models.CharField('محصول',max_length=20,null=False,blank=False)
    description = models.CharField('توضیحات',max_length=50,null=False,blank=False)
    extra_description = models.TextField('توضیحات اضافه',max_length=400,null=False,blank=False)

    amount = models.PositiveSmallIntegerField('مقدار موجود',null=False,blank=False)
    price = models.PositiveIntegerField('قیمت',null=False,blank=False)
    sales = models.SmallIntegerField('فروش',default=0,editable=False)
    discount = models.PositiveIntegerField('تخفیف' , default=0)
    image = models.ImageField('عکس',upload_to=rename_profile_pic)


    slug = models.SlugField(editable=False,blank=True)
    date = models.DateTimeField('تاریخ',auto_now_add=True)

    class Meta :
        verbose_name = 'محصول'
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.title
    
    @property
    def discounted_price(self):
        return self.price - self.discount
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        if len(self.slug) < 1:
            self.slug=random_string(10,True)
        super().save(*args,**kwargs)

class ProductComment(models.Model):
    user = models.ForeignKey('account.User',verbose_name='کاربر',on_delete=models.CASCADE)
    forproduct = models.ForeignKey(Product,verbose_name='برای محصول',on_delete=models.CASCADE)
    comment = models.TextField('کامنت',max_length=80)
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
    
    @property
    def inside_items(self):
        return self.products.count()
    inside_items.fget.short_description = 'تعداد محصول'


def rename_category_pic(instance,filename):
    return rename_file(instance,filename,hardpath='category images')
    
class ProductMainCategory(models.Model):
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE,verbose_name='دسته بندی اصلی')
    image = models.ImageField('عکس',null=False,blank=False ,upload_to=rename_category_pic)

    class Meta :
        verbose_name = 'دسته بندی اصلی محصول'
        verbose_name_plural = "دسته بندی اصلی محصولات"

    @property
    def inside_category_items(self):
        return self.category.inside_items
    inside_category_items.fget.short_description = 'تعداد محصول درون دسته بندی'
