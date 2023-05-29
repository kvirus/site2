from django.urls import path
from sites.views import *

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
    path('rules/', rules, name='rules'),

]



