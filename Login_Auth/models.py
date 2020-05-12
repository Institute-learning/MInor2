from django.db import models
from home.models import Course


# Create your models here.
class Student(models.Model):
	stuName = models.CharField(max_length=50)
	email = models.CharField(max_length=50, primary_key=True)
	password = models.CharField(max_length=50)
	gender = models.CharField(max_length=50)
	dateofBirth = models.DateField()
	#address = models.CharField(max_length=50)
	# enrolledCourses=list of courses elrolled
	#courses = models.ManyToManyField(Course)
	courses1= models.ManyToManyField(Course,blank=True)


class user:
	otp: int
	pwd: str
	Gen: str
	dob: str
	email: str
	name: str	


