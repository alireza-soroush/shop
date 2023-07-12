from django.urls import path
from . import views


urlpatterns = [
    path('',views.blog_page,name='blog_page'),
    path('Blog/<slug:slug>-<str:b_id>',views.blog_object,name='blog_object'),
]