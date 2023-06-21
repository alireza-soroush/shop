from django.urls import path
from . import views


urlpatterns = [
    path('Login',views.login_page,name='login_page'),
    path('Cart',views.cart_page,name='cart_page'),
    path('Receipt',views.checkout_page,name='checkout_page'),
]