from django.shortcuts import render
from .models import Destination,Course

#from ..Quizz.models import Course 

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
    return  render(request,'about.html');

def course(request):
    return  render(request,'course.html');

def courses(request):

    return  render(request,'courses.html');

def contact(request):
    return  render(request,'contact.html');






