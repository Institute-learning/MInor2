from django.shortcuts import render
from .models import Destination
#from ..Quizz.models import Course 

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