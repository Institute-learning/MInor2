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
    return JsonResponse('Payment complete!', safe = False)