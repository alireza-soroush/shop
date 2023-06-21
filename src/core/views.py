from django.shortcuts import render




def homepage(request):
    return render(request,'Index.html',{})

def gallery_page(request):
    return render(request,'gallery.html',{})

def about_page(request):
    return render(request,'about-us.html',{})

def contact_page(request):
    return render(request,'contact-us.html',{})