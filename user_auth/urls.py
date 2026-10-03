from django.urls import path
from .views import *

urlpatterns =[
    path('register/',register,name='register'),
    path('login_/',login_,name='login_'),
    path('logout_/',logout_,name='logout_'),
    path('profile/',profile,name='profile'),
    path('update_profile/',update_profile,name='update_profile'),
    path('reset_pasw/',reset_pasw,name='reset_pasw'),
    path('forget_pasw/',forget_pasw,name='forget_pasw')
]