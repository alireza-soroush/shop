from django import forms
from .models import BlogComment

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('comment',)

class BlogSearch(forms.Form):
    query = forms.CharField(max_length=50)