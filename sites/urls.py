from django.urls import path
from sites.views import *
from django.conf import settings
from django.conf.urls.static import static

from .views import *

app_name = 'sites'

urlpatterns =[
    path('', index, name='index'),
    #path('login/', login, name='login'),
    path('base/', base, name='base'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_exit, name='logout'),
    path('open_1c/', open_1c, name='open_1c'),
    path('close_1c/', close_1c, name='close_1c'),
    path('open_mik/', open_mik, name='open_mik'),
    path('close_mik/', close_mik, name='close_mik'),
    path('mik_res/', mik_res, name='mik_res'),
    path('rules/', rules, name='rules'),
    path('info/', info, name='info'),
    path('menu/', menu, name='menu'),
    path('menus/', menus, name='menus'),
    path('addlink/', addlink, name='addlink'),
    path('phones/', phones, name='phones'),
    path('add_phone/', add_phone, name='add_phone'),
    path('def_test/', def_test, name='def_test'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



