from django.shortcuts import render
from .models import Destination
#from ..Quizz.models import Course 
from .models import Student

# Create your views here.
def index(request):
    return render(request,'index2.html')
    
# Create your views here.

def acont(request):
    dests =Destination.objects.all()

    return render(request,'index2.html', {'dests': dests})

def module(request):
    dests = Destination.objects.all()

    return render(request, 'next2.html', {'dests': dests})


def idk(request):
    c=Student(courseName="sanchit",courseDesc="pta nhi ")
	#c.save()
    c.save()
    return render(request,"hello")
