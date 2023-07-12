from django import forms
from .models import User
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.core.validators import RegexValidator

class Userform(UserChangeForm):
    image=forms.ImageField(required=False ,widget=forms.FileInput())
    class Meta:
        model = User
        fields = ('email','first_name','last_name','gender','image','company','area','state','city','street','house_plate','zipcode','phone')

        

class UserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','first_name','last_name','gender','password1','password2')



class CheckoutForm(UserChangeForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = forms.CharField(validators=[phone_regex], max_length=17,required=True)
    city= forms.CharField(required=True)
    state = forms.CharField(required=True,)
    street = forms.CharField(required=True)
    house_plate = forms.IntegerField(required=True)
    zipcode=forms.IntegerField(required=True)
    class Meta:
        model = User
        fields = ('first_name','last_name','company','area','state','city','street','house_plate','zipcode','phone')