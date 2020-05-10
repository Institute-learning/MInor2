from . import views
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns =[
   
    #path('homeInstitute',views.homeInstitute),
    path('homeMenu',views.homeMenu),
    path('stuSave',views.stuSave),
    path('stuOTP',views.stuOTP),
    path('loginCheckStudent',views.loginCheckStudent),
    path('profile',views.profile),
    path('classRoom',views.classroom),
    path('changepasswordOpen',views.changepasswordOpen),
    path('index',views.index),
    path('homeBack',views.homeBack),
]