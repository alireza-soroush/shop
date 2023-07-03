from django import forms
from .models import User
from django.contrib.auth.forms import UserChangeForm,UserCreationForm

class Userform(UserChangeForm):
    image=forms.ImageField(required=False ,widget=forms.FileInput())
    class Meta:
        model = User
        fields = ('email','first_name','last_name','gender','image','company','area','state','city','street','house_plate','zipcode','phone')

        

class UserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','first_name','last_name','gender','password1','password2')
