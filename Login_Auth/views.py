from django.shortcuts import render, redirect
#from Login_Auth.models import user
from django.core.mail import send_mail 
from django.conf import settings
from django.http import HttpResponse
import random
from home.models import Course
from home.views import index
from django.contrib import messages
from .forms import UserRegisterForms
#from home.models import student1
from django.contrib.auth.models import User




otpGen=0
globalForm = UserRegisterForms

def register(request):
	#form = None 
	global otpGen
	global globalForm
	otpGen=random.randrange(100000,999999)
	if request.method == 'POST':
		form = UserRegisterForms(request.POST)
		globalForm = form
		if form.is_valid():
			username = form.cleaned_data.get('username')
			Email=form.cleaned_data.get("email")
			print(Email)
			messages.success(request, f'Account created for {username}!')
			subject = 'Welcome to E-Learning'
			message = 'Thank you for registering into our E-Learning platform. Your OTP  for verification is '+str(otpGen)
			from_email = settings.EMAIL_HOST_USER	
			to_list = Email
			send_mail(subject,message,from_email,[to_list],fail_silently=False)

			return render(request,'Login_Auth/stuOTP.html',{'email':Email})
			
	else:
			form = UserRegisterForms()
	return render(request,'Login_Auth/register.html', {'form': form})

def stuOTP(request):
	global gobalForm 
	otpGen = request.POST["otp"]
	globalForm.save()
	username = globalForm.cleaned_data.get('username')
	user=User.objects.get(username=username)
	#stud=student1(user=user)
	#stud.save()
	
	return redirect('login') 


