from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   path('home',views.index),
   path('acont',views.module),
   path('content',views.content),
   path('about',views.about),
   path('course',views.course),
   path('courses',views.courses),
   path('contact',views.contact),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)