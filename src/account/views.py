from django.shortcuts import render,redirect
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.decorators import login_required
from .forms import Userform

def login_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('homepage')
    return render(request,'account/login.html',{})


@login_required(login_url='login_page')
def logout_page(request):
    logout(request)
    return redirect('homepage')

def signup_page(request):
    return render(request,'account/sign-up.html',{})

@login_required(login_url='login_page')
def profile_page(request):
    form = Userform(instance=request.user)
    img = request.user.image
    if request.method == 'POST':
        form = Userform(request.POST,request.FILES,instance=request.user)
        if form.has_changed():
            if form.is_valid():
                form.save()
                return redirect('homepage')
            
    return render(request,'account/profile.html',{'form':form,'profile_image':img})

def cart_page(request):
    return render(request,'account/cart.html',{})


def checkout_page(request):
    return render(request,'account/checkout.html',{})