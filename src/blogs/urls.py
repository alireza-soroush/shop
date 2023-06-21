from django.urls import path
from . import views


urlpatterns = [
    path('',views.blog_page,name='blog_page'),
    path('blog',views.blog_object,name='blog_object'),
]