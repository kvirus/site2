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

class addPhone(ModelForm):
    class Meta:
        model = phone
        fields = ['title','phone','job','mail']
        widgets = {
            "title": TextInput(attrs={
                'class':'form-control',
                'placeholder':'ФИО'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            "job": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Должность'
            }),
            "mail": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта'
            }),
        }


class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100)

class PhotoImg(forms.ModelForm):
    class Meta:
        model = phone
        fields = ['photo']

#Расширение стандарной модели админки
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']

