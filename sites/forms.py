from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

class addlinkForm(ModelForm):
    class Meta:
        model = add_links
        fields = ['title','link']
        widgets = {
            "title": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Название ссылки'
            }),
            "link": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка'
            })
        }