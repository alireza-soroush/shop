from django.shortcuts import render
from .models import Blog,BlogViews
from django.core.paginator import Paginator


def blog_page(request):
    #paginate

    order = request.GET.get('order')
    if order:
        if order == 'latest':
            paginate = Blog.objects.order_by('-date')
        elif order == 'oldest':
            paginate = Blog.objects.order_by('date')
        elif order == 'most-viewed':
            all_views = [i for i in Blog.get_views()]
            all_views.sort(key=lambda x: x[1],reverse=True)
            all_views = [i[0] for i in all_views]
            paginate = list(map(lambda id: Blog.objects.get(pk=id), all_views))
        else:
            paginate = Blog.objects.order_by('-date')
    else:
        paginate = Blog.objects.order_by('-date')



    page = request.GET.get('page')
    paginated = Paginator(paginate,6)
    blogs = paginated.get_page(page)

    #recomended
    recommended = Blog.objects.order_by('?')[0:3]
    return render(request,'blogs/blog.html',{'blogs':blogs,'recommended':recommended,'order':order})






def blog_object(request,b_id):
    #get ip
    blog_details=Blog.objects.get(pk=b_id)
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    BlogViews.objects.get_or_create(IPAddres=get_client_ip(request) , blog=blog_details)
    
    #recomended
    recommended = Blog.objects.order_by('?').exclude(pk=b_id)[0:3]
    return render(request,'blogs/page-blog.html',{'blog':blog_details,'recommended':recommended})