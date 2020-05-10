from django.shortcuts import render
from Login_Auth.models import user,Student 
from django.core.mail import send_mail 
from django.conf import settings
from django.http import HttpResponse
import random
from home.models import Course
from home.views import index

# Create your views here.

def homeInstitute(request):
	return render(request,'reg.html')


		
def homeMenu(request):
		return render(request,'studentLogin.html')
			
	

otpGen=0


def stuSave(request):#yeah call hoga
	global otpGen
	otpGen=random.randrange(100000,999999)
	
	StuName=request.POST["name"]
	Password=request.POST["pwd"]
	Gender=request.POST["gender"]
	Dob=request.POST["dob"]
	Email=request.POST["eid"]
	subject = 'Welcome to E-Learning'
	message = 'Thank you for registering into our E-Learning platform. Your OTP  for verification is '+str(otpGen)
	from_email = settings.EMAIL_HOST_USER	
	to_list = Email
	send_mail(subject,message,from_email,[to_list],fail_silently=False)
	
	user1=user()
	#user1.otp=otpGen
	user1.pwd=Password
	user1.Gen=Gender
	user1.dob=Dob
	user1.email=Email
	user1.name=StuName
	
	return render(request,'stuOTP.html',{"user":user1})
	

	
	



def stuOTP(request):
	global optGen

	StuName=request.POST.get('fname')
	Password1=request.POST['pass']
	Gender=request.POST['gen']
	Dob=request.POST['dob']
	Email=request.POST['e_id']
	print(Password1)

	Otp=str(request.POST["otp"])

	if (Otp==str(otpGen)):
		c=Student(stuName=StuName,email=Email,password=Password1,gender=Gender,dateofBirth=Dob)
		c.save()
		# a="<h1>Student Saved</h1>"
		request.session.username=StuName
		return index(request)
    	#
		#)


		#resp=HttpResponse(a)
		#return(resp)
	else:
		a = "<h1>OTP Verification Failed</>"
		resp = HttpResponse(a)
		return (resp)
		
	

def loginCheckStudent(request):
	eid=request.POST["eid"]
	pwd=request.POST["pwd"]
	pwd=pwd+" "
	print(type(Student.email))
	lt=Student.objects.filter(email=eid,password=pwd)
	#print(eid)
	#print("Hello")
	
	if lt:
		request.session["id"]=eid
		request.session["pw"]=pwd
		
		b=lt[0].stuName
		
		request.session.username=b
		c=b.capitalize()
		request.session.modified = True
		print(request.session.username)

		return index(request)
	else:
		return render(request,'retry.html')




def profile(request):
	v='''
	<html>
	<head>
	<meta charset="utf-8"/>
	<meta name="viewport" content="width=device-width,initial-scale=1"/>
	<link rel="stylesheet" href="/static/bootstrap.min.css"/>
	<script src="/static/jquery.min.js"></script>
	<script src="/static/bootstrap.min.js"></script>
	</head>
	<body class="bg-success">
	'''
	StuName=request.session.get("iname")
	#InstName=request.session.get("instName")
	#Batch=request.session.get("btc")
	Email=request.session.get("id")
	stu=Student.objects.filter(email=Email,stuName=StuName)
	#sub=Subject.objects.filter(instName=InstName,batch=Batch,)
	if stu:
		v+="<br><br><div class='container' style=' background-image:url(/static/classbg.jpg)' ><img src='/static/profile.jpg' style='width:20%;' class='img-circle'>"
		v+="<br><h2><font color='white'>"+StuName.capitalize()+ " </font><span class='badge' style='background-color:white;'><span style='color:white;'>&#10004;</span></span></h2><h4><span class='label label-warning'>Student</h4></div>"
		v+="<br><div class='container' ><div class='row'><div class='col-lg-6 bg-info' style='background-color:white;'>"
		#v+="<br><h5 class='bg-success'>&#x1F947;  " +stu[0].batch.capitalize()+"</h5><br>"	
		
		#v+="<h5 class='bg-info'>&#127891;  " +stu[0].instName+"</h5><br>"
		v+="<h5 class='bg-warning'>&#x2709;  " +stu[0].email+"</h5><br>"
		v+="<h5 class='bg-success'>&#x1F382;  " +str(stu[0].dateofBirth)+"</h5><br>"	
		v+="<h5 class='bg-primary'>&#x1F38E;  " +stu[0].gender.capitalize()+"</h5><br>"
		#v+="<h5 class='bg-danger'>&#x1F30D;  " +stu[0].address+"</h5><br></div>"	
		#v+="<br><br><div class='col-lg-6' ><table class='table'><tr><th class='danger'>Subject</th><th class='warning'>Teacher Name</th>"
		#for rec in sub:
		#	v+="<tr><td class='danger'>"+rec.subject+"</td><td class='warning'>"+rec.teacher+"</td>"
		#v+="<table>"
		v+="</div></div></div>"
	resp=HttpResponse(v)
	return(resp)

def classroom(request):
	return render(request,'stuClass.html')

def changepasswordOpen(request):	
	a=request.GET["a"]
	return render(request,'changepassword.html')

def index(request):
	return render(request,'index2.html')

def homeBack(request):
	b=request.GET["a"]
			
	k=request.session.get("iname").capitalize()
	return render(request,'homeStudent.html',{"uname":k})