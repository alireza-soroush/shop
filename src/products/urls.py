from django.urls import path
from . import views


urlpatterns = [
    path('',views.product_page,name='products_page'),
    path('Product-<str:p_id>',views.product_object,name='product_object'),
] 