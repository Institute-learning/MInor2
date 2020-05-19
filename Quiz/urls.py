from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [path('abc/', include('Quizz.urls')),
    path('admin/', admin.site.urls),
    path('access/', include('access.urls')),
    path('', include('home.urls')),
    path('', include('Login_Auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='Login_Auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Login_Auth/logout.html'), name='logout'),
    path('',include('cart.urls')),
   
 ]


# urlpatterns=urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)()
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)