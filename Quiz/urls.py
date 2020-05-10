from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [path('abc/', include('Quizz.urls')),
    path('admin/', admin.site.urls),
    path('access/', include('access.urls')),
    path('', include('home.urls')),
    path('log/',include('Login_Auth.urls'))
 ]


# urlpatterns=urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)()
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)