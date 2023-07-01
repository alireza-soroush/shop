from django import forms
from .models import ProductComment


class ProductCommentsForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ('comment',)