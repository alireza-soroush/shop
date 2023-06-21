from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('Products',include('products.urls')),
    path('Blogs',include('blogs.urls')),
    path('Account/',include('account.urls'))
]
