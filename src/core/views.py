from django.shortcuts import render
from products.models import Product,ProductComment,ProductMainCategory
from blogs.models import Blog



def homepage(request):
    products = Product.objects.order_by('-date')[:8]
    blogs = Blog.objects.order_by('-date')[:4]
    products_comments =  ProductComment.objects.order_by('-date')[:10]
    main_categories = ProductMainCategory.objects.order_by('-id')
    return render(request,'Index.html',{'products':products,'products_comments':products_comments,'blogs':blogs,'main_categories':main_categories})



def gallery_page(request):
    return render(request,'gallery.html',{})

def about_page(request):
    return render(request,'about-us.html',{})

def contact_page(request):
    return render(request,'contact-us.html',{})