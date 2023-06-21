from django.shortcuts import render

def blog_page(request):
    return render(request,'blogs/blog.html',{})


def blog_object(request):
    return render(request,'blogs/page-blog.html',{})