from django.shortcuts import render,redirect
from .models import Blog,BlogViews
from django.core.paginator import Paginator
from .forms import BlogForm
from django.contrib.auth.decorators import login_required


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






def blog_object(request,b_id,slug):
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
    
    #recommended
    recommended = Blog.objects.order_by('?').exclude(pk=b_id)[0:3]

    #Blog comment form
    @login_required(login_url='login_page')
    def blog_comment(request,b_id):
            form = BlogForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.for_blog = Blog.objects.get(pk=b_id)
                obj.save()
                form = BlogForm()
                return True
            else:
                return False
            
    form = BlogForm()
    if request.method == 'POST':
        if request.user.is_authenticated:
            blog_comment(request,b_id)
        else:
            return redirect('login_page')
            
        

    return render(request,'blogs/page-blog.html',{'blog':blog_details,'recommended':recommended,'form':form})


