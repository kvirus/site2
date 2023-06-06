from aiogram.utils.mixins import DataMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.apps import apps
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import *

import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
passwd = "Jac" #Пароль для скриптов!!!


#from .forms import LoginForm

# Create your views here.
from django.urls import reverse_lazy
from sites.forms import LoginForm


def index(request):
    return render(request, 'sites/index.html')

def menu(request):
    return render(request, 'sites/menu.html')

def addlink(request):
    error = ''
    if request.method =='POST':
        form = addlinkForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма не верная'
    form = addlinkForm()
    data = {
        'form':form,
        'error': error
    }
    return render(request, 'sites/addlink.html', data)

#def login(request):
 #   return render(request, 'sites/login.html')

def base(request):
    return render(request, 'sites/base.html')

def rules(request):
    return render(request, 'sites/rules.html')

def info(request):
    return render(request, 'sites/info.html')


def open_1c (request): #Открыть правило для 1С SQL снаружи
    try:
        client.connect(hostname='10.100.2.1', port=6666, username="bka", password=passwd, look_for_keys=False,
                       allow_agent=False)
        _stdin, _stdout, _stderr = client.exec_command('ip firewall nat enable numbers=5')
        return render(request, 'sites/return.html')
        #return HttpResponse("Выполнено")
    except Exception:
        return render(request, 'sites/error.html')

def close_1c (request): #Закрыть правило для 1С SQL снаружи
    try:
        client.connect(hostname='10.100.2.1', port=6666, username="bka", password=passwd, look_for_keys=False,
                       allow_agent=False)
        _stdin, _stdout, _stderr = client.exec_command('ip firewall nat disable numbers=5')
        return render(request, 'sites/return.html')
        #return HttpResponse("Выполнено")
    except Exception:
        return render(request, 'sites/error.html')

def open_mik (request): #Закрыть правило для mikrotik снаружи
    try:
        client.connect(hostname='10.100.2.1', port=6666, username="bka", password=passwd, look_for_keys=False,
                       allow_agent=False)
        _stdin, _stdout, _stderr = client.exec_command('ip firewall nat enable numbers=2')
        return render(request, 'sites/return.html')
        #return HttpResponse("Выполнено")
    except Exception:
        return render(request, 'sites/error.html')


def close_mik (request): #Закрыть правило для mikrotik снаружи
    try:
        client.connect(hostname='10.100.2.1', port=6666, username="bka", password=passwd, look_for_keys=False,
                       allow_agent=False)
        _stdin, _stdout, _stderr = client.exec_command('ip firewall nat disable numbers=2')
        return render(request, 'sites/return.html')
        #return HttpResponse("Выполнено")
    except Exception:
        return render(request, 'sites/error.html')


# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#     else:
#         form = LoginForm()
#     return render(request, 'sites/login.html', {'sites:form': form})

# class LoginUser(DataMixin, LoginView):
#     form_class = AuthenticationForm
#     template_name = 'sites/login.html'

    #
    # def get_context_data(self, *, object_list=None, **kwargs):
    #      context = super().get_context_data(**kwargs)
    #      c_def = self.get_user_context(title="Авторизация")
    #      return dict(list(context.items()) + list(c_def.items()))
class CustomLoginView(LoginView):
    authentication_form = AuthenticationForm
    template_name = 'sites/login.html'

    def get_success_url(self):
        return reverse_lazy('sites:index')

def logout_exit(request):
    logout(request)
    return redirect('index')