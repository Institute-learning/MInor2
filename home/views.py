from django.shortcuts import render
from .models import Course,Module,quiz,question,student1,studyMat
#from ..Quizz.models import Course
#from Login_Auth.models import Student
from django.contrib.auth.models import User



# Create your views here.
def index(request):
    dests = Course.objects.all()


    #l=Student.objects.all()
    #print(l[0].courses1.all()[0].courseName)
    return render(request,'index.html', {'dests': dests})
    
# Create your views here.

def acont(request):
    dests = Course.objects.all()

    return render(request, 'index.html', {'dests': dests})


def module(request):
    dests = Course.objects.all()

    return render(request, 'next2.html', {'dests': dests})


def idk(request):
    c = Student(courseName="sanchit", courseDesc="pta nhi ")
    # c.save()
    c.save()
    return render(request, "hello")


def about(request):
    return render(request, 'vid.html')


def course(request):
    if (request.method == 'POST'):
        name = request.POST["na"]
        print(name)
        print(request.user.id)
        dests = Course.objects.filter(courseName=name)
        # print(dests)
        id = Course.objects.only('id').get(courseName=name).id
        Uid = request.user.id
        stud=student1.objects.filter(user1=Uid)
        cname=stud[0].courses.filter(courseName=name)
        if(cname):
            bought=True
        else:
            bought=False
        modules = Module.objects.filter(course= id)
        

    return render(request, 'courses.html', {'dests': dests, 'mods': modules,'bought':bought})


def content(request):
    dests = Course.objects.all()



def courses(request):
    dests = Course.objects.all()

    return  render(request,'course.html',{'dests':dests})

def contact(request):
    return render(request, 'contact.html')


def idk(request):
    c = Course(courseName="sanchit", courseDesc="pta nhi ")
    # c.save()
    c.save()
    return render(request, "hello")


def check12(request, name):
    return (request, name)


def cart(request):
    return render(request, 'cart_page.html')


def vid(request):
    if (request.method == 'POST'):
        name = request.POST["na"]
        print(name)
        #print(request.user.id)
        dests = Course.objects.filter(courseName=name)

        id = Course.objects.only('id').get(courseName=name).id
        modules=Module.objects.filter(course=id)
        #modules=Course.module.all()
        print("hello")
        #print(modules)
        mods=[]
        for m in modules :
            stu=[]
            print(m.id)
            st=studyMat.objects.filter(module=m.id)
            for s in st :
                stu.append(s)
            #mods.append(stu)
            d={'mo':m,'so':stu}
            mods.append(d)

    
        for x in mods :
            print (x["mo"].moduleName)

    return render(request, 'vid.html' ,{"mods":mods})
