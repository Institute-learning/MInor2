from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url


urlpatterns = [
   path('home',views.index),
   path('acont',views.module),
   path('content',views.content),
   path('about',views.about),
   #path('course',views.course),
   path('courses',views.courses),
   path('contact',views.contact),
   #path('check',views.check12),
   url(r'^course/$',views.course),
]


# urlpatterns = patterns('',
#     url(r'^check/$', 'views.check12'),
#     )

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
