from django.shortcuts import render
from .models import Destination, Course
#from ..Quizz.models import Course
from .models import Student

# Create your views here.
def index(request):
    dests = Course.objects.all()
    return render(request,'index.html', {'dests': dests})
    
# Create your views here.

def acont(request):
    dests =Course.objects.all()

    return render(request,'index.html', {'dests': dests})

def module(request):
    dests = Course.objects.all()

    return render(request, 'next2.html', {'dests': dests})


def idk(request):
    c=Student(courseName="sanchit",courseDesc="pta nhi ")
	#c.save()
    c.save()
    return render(request,"hello")

def content(request):
    dests = Course.objects.all()

    return render(request, 'coursepage.html', {'dests': dests})

def courses(request):
    dests = Course.objects.all()

    return render(request, 'courses.html', {'dests': dests})

def course(request):
    dests = Course.objects.all()

    return render(request, 'course.html', {'dests': dests})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')