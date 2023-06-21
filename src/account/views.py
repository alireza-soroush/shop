from django.shortcuts import render




def login_page(request):
    return render(request,'account/login.html',{})


def cart_page(request):
    return render(request,'account/cart.html',{})


def checkout_page(request):
    return render(request,'account/checkout.html',{})