from django.db import models
from django.contrib.auth.models import User
from home.models import Course ,student1
#from Login_Auth.models import Profile  
# Create your models here.

class Order(models.Model):
    userProfile = models.ForeignKey(student1, on_delete = models.SET_NULL, blank = True, null = True)
    date_ordered = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default=False, blank = True, null = True)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        total= 0
        orderitems = self.orderitem_set.all()
        total = orderitems.count()
        return total

class OrderItem(models.Model):
	course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.course.price
		return total
	
