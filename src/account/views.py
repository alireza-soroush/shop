from django.shortcuts import render,redirect
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.decorators import login_required
from .forms import Userform,UserCreation
from django.contrib import messages
from products.models import Product
from .models import CartItem
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
def add_to_cart(request, p_id):
    product = Product.objects.get(id=p_id)
    if product.amount > 0:
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        if not created:
            if product.amount <= cart_item.quantity:
                messages.error(request,'متاسفانه مقدار بیشتر در انبار موجود نمیباشد.')
            else:
                cart_item.quantity += 1
                cart_item.save()            
    else:
        messages.error(request,'متاسفانه مقدار بیشتر در انبار موجود نمیباشد.')
    return redirect('cart_page')

@login_required(login_url='login_page')
def remove_from_cart(request, p_id):
    product = Product.objects.get(id=p_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        if cart_item.quantity <= 1:
            cart_item.delete()
        else:
            cart_item.quantity -= 1
            cart_item.save()
    return redirect('cart_page')



def check_product_quantity(items):
    for p in items:
        product = Product.objects.get(pk=p.product.id)
        if product.amount < p.quantity:
            if product.amount == 0:
                p.delete()
            else:
                p.quantity = product.amount
                p.save()

@login_required(login_url='login_page')
def cart_page(request):
    cart_items = CartItem.objects.filter(user=request.user)
    check_product_quantity(cart_items)
    cart_items = CartItem.objects.filter(user=request.user) #for updating cart items after changing in check_product_quantity function
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    total_discount = sum(item.product.discount * item.quantity for item in cart_items)
    final_price = total_price - total_discount
    return render(request,'account/cart.html',{'cart_items': cart_items,'total_price': total_price,'total_discount':total_discount,'final_price':final_price})

@login_required(login_url='login_page')
def checkout_page(request):
    return render(request,'account/checkout.html',{})