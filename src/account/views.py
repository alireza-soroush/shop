from django.shortcuts import render,redirect
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.decorators import login_required
from .forms import Userform,UserCreation



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
def cart_page(request):
    return render(request,'account/cart.html',{})

@login_required(login_url='login_page')
def checkout_page(request):
    return render(request,'account/checkout.html',{})