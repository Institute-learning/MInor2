from django.shortcuts import render
from home.models import Course
from .models import * 
from django.http import JsonResponse
import json

# Create your views here.
def cart(request):
    if request.user.is_authenticated:
        stu_profile = request.user.profile
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
    stu_profile = request.user.profile
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
    stu_profile = request.user.profile
    print(stu_profile)
    cardName = data['card']['Cname']
    cardNo = data['card']['Cno']
    cardType = data['card']['Ctype']
    cardExp = data['card']['Edate']
    u1= User.objects.get(username=stu_profile)
    p=Profile.objects.get(user = u1)
    print('profile:')
    print(p.enrolledCourses)
    o = Order.objects.get(userProfile = p)
    print('orders:')
    print(o)
    oi=[]
    oi= OrderItem.objects.filter(order = o)
    print('Order I:')
    for oe in oi:
        print(oe.course.courseName)
        p.enrolledCourses.add(oe.course)
    u2= User.objects.get(username=stu_profile)
    p1=Profile.objects.filter(user = u2)
    j=p1[0].enrolledCourses.all()
    for i in j:
        print(i.courseName)

    return JsonResponse('Payment complete!', safe = False)