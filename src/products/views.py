from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Product,ProductCategory,ProductComment
from django.core.paginator import Paginator
from .forms import ProductCommentsForm
from django.contrib.auth.decorators import login_required

def product_page(request):
    #categories
    categories = ProductCategory.objects.all()[:5]
    category = request.GET.get('category')
    order = request.GET.get('order')
    print(order)
    #products
    if category:
        p_category = ProductCategory.objects.get(pk=category)
        paginate = p_category.products.all()
    elif order:
        if order=='latest':
            paginate = Product.objects.order_by('-date')
        elif order == 'expensive':
            paginate = Product.objects.order_by('-price')
        elif order == 'cheap':
            paginate = Product.objects.order_by('price')
        elif order == 'most-sales':
            paginate = Product.objects.order_by('-sales')
        
        else:
            paginate = Product.objects.order_by('-date')

    else:
        paginate = Product.objects.order_by('-date')

    #paginate
    paginated = Paginator(paginate,6)
    page = request.GET.get('page')
    products = paginated.get_page(page)

    
    return render(request,'products/shop.html',{'products':products,'categories':categories,'category':category,'order':order})


def product_object(request,p_id):
    product = Product.objects.get(pk=p_id)
    products = Product.objects.all().filter(~Q(id=p_id)).order_by('?')[:5]

    #Comments for Product
    @login_required(login_url='login_page')
    def product_comment(request,p_id):
            form = ProductCommentsForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.forproduct = Product.objects.get(pk=p_id)
                obj.save()
                form = ProductCommentsForm()
                return True
            else:
                return False
            
    form = ProductCommentsForm()
    if request.method == 'POST':
        if request.user.is_authenticated:
            product_comment(request,p_id)
        else:
            return redirect('login_page')
    
    comments = ProductComment.objects.filter(forproduct_id=p_id)
    return render(request,'products/page-shop.html',{'product':product,'products':products,'form':form,'comments':comments})