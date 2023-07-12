from django.urls import path
from . import views
from account.views import updatecart


urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('UpdateCart/',updatecart,name='update_cart'),
    path('Gallery',views.gallery_page,name='gallery_page'),
    path('About-Us',views.about_page,name='about_page'),
    path('Contact-Us',views.contact_page,name='contact_page'),
]
