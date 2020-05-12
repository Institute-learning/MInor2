from django.db import models
from django.contrib.auth.models import User



class Course(models.Model):
	courseName= models.CharField(max_length=50, default=" ")
	courseDesc= models.TextField(default=" ")
	courseImage= models.ImageField(upload_to='pics2/', default=" ")
	price=models.IntegerField(default="100")
	bought=models.BooleanField(default=True)




class Module(models.Model):
	moduleName=models.CharField(max_length=50,default=" ")
	course=models.ForeignKey(Course,on_delete=models.CASCADE,default=1)
	#file1=models.FileField(upload_to='files12/',default=" ")
	#quizz
	#material

class studyMat(models.Model):
	module=models.ForeignKey(Module,on_delete=models.CASCADE,default=1)
	Title=models.CharField(max_length=50,default=" ")
	ls = (
		("video","video"),
		("pdf","pdf"),
		("doc","doc"),
	)

	typ=models.CharField(max_length=6,choices=ls,default="video")
    #typ=models.CharField(max_length=6,choices=types,default=video)
	#)
	file1=models.FileField(upload_to='files12/',default=" ")


class quiz(models.Model):
	quizName=models.CharField(max_length=50,default=" ")
	module=models.ForeignKey(Module,on_delete=models.CASCADE,default=1)

class question(models.Model):
	quizName=models.ForeignKey(quiz,on_delete=models.CASCADE,default=1)
	ques=models.CharField(max_length=100,default=" ")
	option1=models.CharField(max_length=50,default=" ")
	option2=models.CharField(max_length=50,default=" ")
	option3=models.CharField(max_length=50,default=" ")
	option4=models.CharField(max_length=50,default=" ")
	ls=(
		("option1","option1"),
		("option2","option2"),
		("option3","option3"),
		("option4","option4"),
	)

	correctoption=models.CharField(max_length=50,choices=ls,default=option1)


