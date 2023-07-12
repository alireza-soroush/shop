from django.shortcuts import render,redirect
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.decorators import login_required
from .forms import Userform,UserCreation,CheckoutForm
from django.contrib import messages
from products.models import Product
from .models import CartItem
from django.http import JsonResponse
import json


def login_page(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request,email=email,password=password)
            if user is not None:
                login(request,user)
                return redirect('homepage')
            else:
                messages.warning(request,'ایمیل یا رمز عبور اشتباه است.')
        return render(request,'account/login.html',{})


@login_required(login_url='login_page')
def logout_page(request):
    logout(request)
    return redirect('homepage')


def signup_page(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    
    else:
        form = UserCreation
        if request.method == 'POST':
            form = UserCreation(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data['email']
                password = form.cleaned_data['password1']
                user = authenticate(email=email , password=password)
                if user is not None:
                    login(request,user)
                    return redirect('homepage')
        return render(request,'account/sign-up.html',{'form':form})


@login_required(login_url='login_page')
def profile_page(request):
    form = Userform(instance=request.user)
    if request.method == 'POST':
        form = Userform(request.POST,request.FILES,instance=request.user)
        if form.has_changed():
            if form.is_valid():
                form.save()
                return redirect('homepage')
    return render(request,'account/profile.html',{'form':form,})


@login_required(login_url='login_page')
def updatecart(request):
    data=json.loads(request.body)
    productid= data['productId']
    action = data['action']
    product=Product.objects.get(id=productid)
    Item,created= CartItem.objects.get_or_create(user=request.user, product=product,)
    if action=='add':
        if product.amount > Item.quantity:
            Item.quantity += 1
    elif action=='remove':
        Item.quantity -= 1 
    else:
        return JsonResponse('Wrong operation',safe=False)
    Item.save()
    if Item.quantity <= 0:
        Item.delete()
    return JsonResponse('Item was updated',safe=False)

@login_required(login_url='login_page')
def cart_page(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    total_discount = sum(item.product.discount * item.quantity for item in cart_items)
    final_price = total_price - total_discount
    
    for item in cart_items:
        product = Product.objects.get(pk=item.product.id)
        if item.quantity > product.amount:
            item.quantity = product.amount
            item.save()

    return render(request,'account/cart.html',{'cart_items': cart_items,'total_price': total_price,'total_discount':total_discount,'final_price':final_price})



@login_required(login_url='login_page')
def checkout_page(request):
    order_items = CartItem.objects.filter(user=request.user)
    final_price = sum(item.product.discounted_price * item.quantity for item in order_items)
    if final_price <=0:
        return redirect('products_page')
    


    form = CheckoutForm(instance=request.user)

    #payment
    if request.method == 'POST':
        form = CheckoutForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            #Bank payment API
            #
        
        
    return render(request,'account/checkout.html',{'orders':order_items,'final_price':final_price,'form':form})