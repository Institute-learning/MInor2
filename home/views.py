from django.shortcuts import render
from .models import Destination,Course

#from ..Quizz.models import Course 
from .models import Course

# Create your views here.
def index(request):
    dests = Course.objects.all()
    return render(request,'index.html', {'dests': dests})
    
# Create your views here.

def acont(request):
    dests =Destination.objects.all()

    return render(request,'index.html', {'dests': dests})

def module(request):
    dests = Destination.objects.all()

    return render(request, 'next2.html', {'dests': dests})

def content(request):
    dests = Destination.objects.all()

    return render(request, 'coursepage.html', {'dests': dests})

def about(request):
    return  render(request,'about.html')


def course(request):
    if(request.method== 'POST'):
        name=request.POST["na"]
        print(name)
    return  render(request,'course.html')

def courses(request):

    return  render(request,'courses.html')

def contact(request):
    return  render(request,'contact.html')


def idk(request):
    c=Course(courseName="sanchit",courseDesc="pta nhi ")
	#c.save()
    c.save()
    return render(request,"hello")


def check12(request,name):

    return (request,name)