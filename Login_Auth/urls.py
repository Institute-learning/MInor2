from . import views
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns =[
   
 
    path('stuOTP',views.stuOTP),
  
    path('register',views.register,name = 'register'),
]
