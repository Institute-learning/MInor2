from django.shortcuts import render
from .models import Course,Module,quiz,student1,studyMat,question,scorecard
#from ..Quizz.models import Course
#from Login_Auth.models import Student
from django.contrib.auth.models import User
from django.conf import settings
from django.http import HttpResponse


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
        if(stud):
            cname=stud[0].courses.filter(courseName=name)
            if(cname):
                bought=True
            else:
                bought=False
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
        mname=request.POST["nam"]
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
            print("fuck")
            st=studyMat.objects.filter(module=m.id)
            qu=quiz.objects.filter(module=m.id)
            for s in st :
                stu.append(s)
                # print(s.fileNo)
            stu = sorted(stu , key = lambda x: x.fileNo)
            #mods.append(stu)
            for i in qu :
                print(i.id)
            d={'mo':m,'so':stu,'qo':qu}
            mods.append(d)
            
        if(mname=='sanchit'):
            mname=mods[0]["mo"].moduleName
            print(mname)

    
        

    return render(request, 'vid.html' ,{"mods":mods,"mname":mname})


def quiz1(request):
    aid=request.POST["qid"]
    print("quizz")
    print(aid)
    ques1 = question.objects.filter(quiz=aid)
    for i in ques1 :
        print(i.id)
    return render(request,'quizSetup.html',{"ques1":ques1,"qid":aid})

    

def score(request):
    id1=request.POST["qid"]
    s=0
    que=[]
    sid=request.user.id
    sc=scorecard.objects.filter(quiz=id1,student=sid)
    q1=quiz.objects.filter(id=id1)
    s1=student1.objects.filter(user1=id1)
    t=0
    ques1 = question.objects.filter(quiz=id1)
    for q in ques1 :
        a=request.POST.get(str(q.id))
        print(q.correctoption)
        print(a)
        abc={"your":a,"ques":q}
        t=t+1
        if q.correctoption == a:
            s =	s+1
            print(s)
        que.append(abc)

    print('Score:',s)
    p=s/t*100
    sc=scorecard(quiz=q1[0],student=s1[0],attempt=1,totalQues=t,correctAns=s,percentScore=p)
    sc.save()
    return render(request, 'scorecardInstructor.html', {"score":s,"que":que})