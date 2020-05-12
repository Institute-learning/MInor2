from django.shortcuts import render
from .models import Course
#from ..Quizz.models import Course
from Login_Auth.models import Student

# Create your views here.
def index(request):
    dests = Course.objects.all()
    #print(request.session.username)
    request.session.modified = True
    na=request.session.get("username")
    print(na)
    #na=na+" "
    l=Student.objects.all()
    print(l[0].courses1.all()[0].courseName)
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

def about(request):
    return  render(request,'about.html')


def course(request):
    if(request.method== 'POST'):
        
        name=request.POST["na"]
        print(name)
        dests = Course.objects.filter(courseName=name)
        # print(dests.id)

    return  render(request,'courses.html',{'dests':dests})


def content(request):
    dests = Course.objects.filter()

    return render(request, 'coursepage.html', {'dests': dests})

def courses(request):
    dests = Course.objects.all()

    return  render(request,'course.html',{'dests':dests})

def contact(request):
    return  render(request,'contact.html')


def idk(request):
    c=Course(courseName="sanchit",courseDesc="pta nhi ")
	#c.save()
    c.save()
    return render(request,"hello")


def check12(request,name):

    return (request,name)

def cart(request):
    return render(request,'cart_page.html')

    
def vid(request):
    return render(request,'vid.html')
    