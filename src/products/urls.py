from django.urls import path
from . import views


urlpatterns = [
    path('',views.product_page,name='products_page'),
    path('/Product',views.product_object,name='product_object'),
] 