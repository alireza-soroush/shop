from django.urls import path
from . import views


urlpatterns = [
    path('Login',views.login_page,name='login_page'),
    path('Logout',views.logout_page,name='logout_page'),
    path('Sign-Up',views.signup_page,name='signup_page'),
    path('Profile',views.profile_page,name='profile_page'),
    path('Delete-Profile-Image',views.remove_profile_pic,name='remove_profile_image'),
    path('Cart',views.cart_page,name='cart_page'),
    path('Checkout',views.checkout_page,name='checkout_page'),
]