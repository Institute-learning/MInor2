from django.shortcuts import render
from home.models import Course
from .models import Order, OrderItem 
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from .models import Course,student1


# Create your views here.
def cart(request):
    if request.user.is_authenticated:
        stu_profile = request.user.student1
        order, created = Order.objects.get_or_create(userProfile = stu_profile, complete = False  )
        items = order.orderitem_set.all()
    else:
        items = []
        order = []
    context = {'items':items, 'order': order}
    return render(request,'cart/cart.html',context)

def updateItem(request):
    data = json.loads(request.body)
    courseName = data['courseName']
    action = data['action']
    print('Action1:', action)
    print('Course:', courseName)
    stu_profile = request.user.student1
    course = Course.objects.get(courseName=courseName)
    order, created = Order.objects.get_or_create(userProfile=stu_profile, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, course=course)
    if action == 'add':
        orderItem.save()
        print('added')
    elif action == 'remove':
        print('remove')
        orderItem.delete()
        
    return JsonResponse('Item was added', safe=False)

def checkout(request):
    data = json.loads(request.body)
    print("hello")
    print(data)
    StuFname=data['form']['Fname']
    StuLname=data['form']['Lname']
    user = data['form']['user']

    print(StuFname)
    print(StuLname)
    stu_profile = request.user.student1
    print(stu_profile.user1.username)
    print('WTF:')
    cardName = data['card']['Cname']
    cardNo = data['card']['Cno']
    cardType = data['card']['Ctype']
    cardExp = data['card']['Edate']
    u1= User.objects.get(username=stu_profile.user1.username)
    p=student1.objects.get(user1 = u1)
    print('profile:')
    print(p.courses)
    o = Order.objects.get(userProfile = p,complete = False)
    o.complete = True
    o.save()
    print('orders:')
    print(o)
    oi=[]
    oi= OrderItem.objects.filter(order = o)
    print('Order I:')
    for oe in oi:
        print(oe.course.courseName)
        p.courses.add(oe.course)
    u2= User.objects.get(username=stu_profile.user1.username)
    p1=student1.objects.filter(user1 = u2).first()
    j=p1.courses.all()
    for i in j:
        print(i.courseName)
    print('THE END')



    return JsonResponse('Payment complete!', safe = False)