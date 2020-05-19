from . import views
from django.urls import path,include

urlpatterns =[
   
 
    path('cart',views.cart,name = 'cart'),
    path('update_item',views.updateItem, name='update_item'),
    path('checkout',views.checkout),
    ]
