from django.db import models
from django.contrib.auth.models import User

class stud(User):
	sub=models.CharField(max_length=50,default=" ")

class Destination(models.Model):
    name= models.CharField(max_length=50, default=" ")
    img= models.ImageField(upload_to='pics2/', default=" ")
    desc= models.TextField(default=" ")
    price= models.IntegerField(default="100")
    bought= models.BooleanField(default=True)
    destno = models.IntegerField(default="0")


class Course(models.Model):
	courseName= models.CharField(max_length=50, default=" ")
	courseDesc= models.TextField(default=" ")
	courseImage= models.ImageField(upload_to='pics2/', default=" ")
	price=models.IntegerField(default="100")
	bought=models.BooleanField(default=True)
	#courseId

# modules

class Student(models.Model):
	# instName=models.CharField(max_length=50)
	stuName = models.CharField(max_length=50)
	email = models.CharField(max_length=50, primary_key=True)
	password = models.CharField(max_length=50)
	# batch=models.CharField(max_length=50)
	gender = models.CharField(max_length=50)
	dateofBirth = models.DateField()
	address = models.CharField(max_length=50)
	# enrolledCourses=list of courses elrolled
	courses= models.ManyToManyField(Course,blank=True)



class Module(models.Model):
	moduleName=models.CharField(max_length=50,default=" ")
	course=models.ForeignKey(Course,on_delete=models.CASCADE,default=1)
	file1=models.FileField(upload_to='files12/',default=" ")
	#content
	#quizId if any
	#material


class Quiz(models.Model):
	#instName=models.CharField(max_length=50)
	quizName=models.CharField(max_length=50)
	#module=models.ForeignKey(Module,on_delete=models.CASCADE)
	#batch=models.CharField(max_length=50)
	#subject=models.CharField(max_length=50)
	#teacher=models.CharField(max_length=50)
	question=models.CharField(max_length=50)
	ans1=models.CharField(max_length=50)
	ans2=models.CharField(max_length=50)
	ans3=models.CharField(max_length=50)
	ans4=models.CharField(max_length=50)
	correct=models.CharField(max_length=50)
	points=models.IntegerField(default=1)



class ReadyQuiz(models.Model):
	# class Meta:
	# 	unique_together=(('instName','batch','subject','quizName'))
	instName=models.CharField(max_length=50)
	quizName=models.CharField(max_length=50)
	batch=models.CharField(max_length=50)
	subject=models.CharField(max_length=50)
	teacher=models.CharField(max_length=50)
	attempts=models.CharField(max_length=50)
	time=models.CharField(max_length=50)

class QuizResult(models.Model):
	instName=models.CharField(max_length=50)
	quizName=models.CharField(max_length=50)
	batch=models.CharField(max_length=50)
	subject=models.CharField(max_length=50)
	teacher=models.CharField(max_length=50)
	correctAnswer=models.CharField(max_length=50)
	totalPoints=models.CharField(max_length=50)
	quizDate=models.DateField(max_length=50)
	quizTime=models.CharField(max_length=50)
	stuEmail=models.CharField(max_length=50)
	totalQues=models.CharField(max_length=50)

class StudyFolder(models.Model):
	# class Meta:
	# 	unique_together=(('instName','batch','subject','teacherEmail','folderName'))
	#instName=models.CharField(max_length=50)
	#batch=models.CharField(max_length=50)
	#subject=models.CharField(max_length=50)
	teacherEmail=models.CharField(max_length=50)
	folderName=models.CharField(max_length=50)









#
# class Institute(models.Model):
# 	instName=models.CharField(max_length=50)
# 	password=models.CharField(max_length=50)
# 	type=models.CharField(max_length=50)
# 	email=models.CharField(max_length=50,primary_key=True)
# 	address=models.CharField(max_length=150)
# 	city=models.CharField(max_length=150)
# 	contact=models.CharField(max_length=150)
# class Batch(models.Model):     #course
# 	class Meta:
# 		unique_together=(('instName','batchName'))
# 	instName=models.CharField(max_length=50)
# 	batchName=models.CharField(max_length=50,primary_key=True)    #course name
#
# class Student(models.Model):
# 	instName=models.CharField(max_length=50)
# 	stuName=models.CharField(max_length=50)
# 	email=models.CharField(max_length=50,primary_key=True)
# 	password=models.CharField(max_length=50)
# 	batch=models.CharField(max_length=50)		#nhi aayega list of courses
# 	gender=models.CharField(max_length=50)
# 	dateofBirth=models.DateField()
# 	address=models.CharField(max_length=50)
# 	#pyament info
#
# class Subject(models.Model):			# udega
# 	class Meta:
# 		unique_together=(('instName','batch','subject'))
# 	instName=models.CharField(max_length=50)
# 	batch=models.CharField(max_length=50)
# 	subject=models.CharField(max_length=50)
# 	teacher=models.CharField(max_length=50)
# 	teacherEmail=models.CharField(max_length=50)
#
# class Instructor(models.Model):
# 	instName=models.CharField(max_length=50)
# 	Name=models.CharField(max_length=50)
# 	email=models.CharField(max_length=50,primary_key=True)
# 	password=models.CharField(max_length=50)
# 	gender=models.CharField(max_length=50)
# 	dateofBirth=models.DateField()
# 	address=models.CharField(max_length=50)
# 	designation=models.CharField(max_length=50)			# hata sakte hai
#
# class Quiz(models.Model):
# 	instName=models.CharField(max_length=50)
# 	quizName=models.CharField(max_length=50)
# 	batch=models.CharField(max_length=50)
# 	subject=models.CharField(max_length=50)
# 	teacher=models.CharField(max_length=50)
# 	question=models.CharField(max_length=50)
# 	ans1=models.CharField(max_length=50)
# 	ans2=models.CharField(max_length=50)
# 	ans3=models.CharField(max_length=50)
# 	ans4=models.CharField(max_length=50)
# 	correct=models.CharField(max_length=50)
# 	points=models.IntegerField(default=1)
#
# class ReadyQuiz(models.Model):
# 	class Meta:
# 		unique_together=(('instName','batch','subject','quizName'))
# 	instName=models.CharField(max_length=50)
# 	quizName=models.CharField(max_length=50)
# 	batch=models.CharField(max_length=50)
# 	subject=models.CharField(max_length=50)
# 	teacher=models.CharField(max_length=50)
# 	attempts=models.CharField(max_length=50)
# 	time=models.CharField(max_length=50)
#
# class QuizResult(models.Model):
# 	instName=models.CharField(max_length=50)
# 	quizName=models.CharField(max_length=50)
# 	batch=models.CharField(max_length=50)
# 	subject=models.CharField(max_length=50)
# 	teacher=models.CharField(max_length=50)
# 	correctAnswer=models.CharField(max_length=50)
# 	totalPoints=models.CharField(max_length=50)
# 	quizDate=models.DateField(max_length=50)
# 	quizTime=models.CharField(max_length=50)
# 	stuEmail=models.CharField(max_length=50)
# 	totalQues=models.CharField(max_length=50)
#
# class StudyFolder(models.Model):
# 	class Meta:
# 		unique_together=(('instName','batch','subject','teacherEmail','folderName'))
# 	instName=models.CharField(max_length=50)
# 	batch=models.CharField(max_length=50)
# 	subject=models.CharField(max_length=50)
# 	teacherEmail=models.CharField(max_length=50)
# 	folderName=models.CharField(max_length=50)
#