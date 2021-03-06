from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url


urlpatterns = [
   path('home',views.index, name = 'home'),
   path('mycourse',views.mycourse,name='mycourse'),
   path('acont',views.module),
   path('tp',views.idk),
   url(r'about/$',views.about,name="about"),
   #path('course',views.course),
   path('courses',views.courses, name = 'courses'),
   path('contact',views.contact),
   #path('check',views.check12),
   #path('cart',views.cart,name="cart"),
   url(r'^quiz/$',views.quiz1,name="quiz"),
   url(r'^score/$',views.score,name="score"),
   url(r'^course/$',views.course),
   url(r'^vid/$',views.vid,name='vid'),
   url(r'^progress/$',views.progress,name='progress'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
