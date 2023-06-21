from django.shortcuts import render

def product_page(request):
    return render(request,'products/shop.html',{})

def product_object(request):
    return render(request,'products/page-shop.html',{})