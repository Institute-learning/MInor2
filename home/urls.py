from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url


urlpatterns = [
   path('home',views.index),
   path('acont',views.module),
   path('tp',views.idk),
   
   path('content',views.content),
   path('about',views.about),
   #path('course',views.course),
   path('courses',views.courses),
   path('contact',views.contact),
   #path('check',views.check12),
   path('cart',views.cart),
   url(r'^course/$',views.course),
   path('vid',views.vid),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
