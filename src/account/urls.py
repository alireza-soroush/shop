from django.urls import path
from . import views


urlpatterns = [
    path('Login',views.login_page,name='login_page'),
    path('Logout',views.logout_page,name='logout_page'),
    path('Sign-Up',views.signup_page,name='signup_page'),
    path('Profile',views.profile_page,name='profile_page'),
    path('Cart',views.cart_page,name='cart_page'),
    path('Add-To-Cart/<int:p_id>',views.add_to_cart,name='add_to_cart'),
    path('Remove-From-Cart/<int:p_id>',views.remove_from_cart,name='remove_from_cart'),
    path('Receipt',views.checkout_page,name='checkout_page'),
]