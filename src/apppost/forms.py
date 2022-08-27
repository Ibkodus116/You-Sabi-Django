from django import forms
from django.forms import ModelForm
from .models import Post

class Postform(ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'headline', 'contex', 'date')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control w-25 p-3'}),
            'headline': forms.TextInput(attrs={'class':'form-control w-25 p-3'}),
            'contex': forms.Textarea(attrs={'class':'form-control w-25 p-3'}),
        }