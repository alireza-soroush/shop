from django.shortcuts import render
from products.models import Product,ProductComment,ProductMainCategory
from blogs.models import Blog
from products.models import Product
from datetime import datetime

def homepage(request):
    products = Product.objects.order_by('-date')[:8]
    blogs = Blog.objects.order_by('-date')[:4]
    products_comments =  ProductComment.objects.order_by('-date')[:10]
    main_categories = ProductMainCategory.objects.order_by('-id')
    return render(request,'Index.html',{'products':products,'products_comments':products_comments,'blogs':blogs,'main_categories':main_categories})



def gallery_page(request):
    return render(request,'gallery.html',{})

def about_page(request):
    products = Product.objects.count()
    experience = datetime.now().year - 2008
    customers = sum([product.sales for product in Product.objects.all()])
    return render(request,'about-us.html',{'products':products,'experience':experience,'customers':customers})

def contact_page(request):
    return render(request,'contact-us.html',{})