"""Classic_JP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('aplicaciones.usuario.urls'), name="usuarios"),
    path('producto/', include('aplicaciones.producto.urls'), name="producto"),
    #paths de login
    path('login/',auth_views.LoginView.as_view(template_name='usuario/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='usuario/logout.html'), name='logout'),
    #paths de recuperacion de contraseñas
    path('recuperacion-contraseña',auth_views.PasswordResetView.as_view(template_name='usuario/password_reset.html'), name='password_reset'),
    path('recuperacion-contraseña/continuar',auth_views.PasswordResetDoneView.as_view(template_name='usuario/password_reset_done.html'), name='password_reset_done'),
    path('recuperacion-contraseña-confirmar/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='usuario/password_reset_confirm.html'), name='password_reset_confirm'),
    path('recuperacion-contraseña-exitoso',auth_views.PasswordResetCompleteView.as_view(template_name='usuario/password_reset_complete.html'), name='password_reset_complete'),
    


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
