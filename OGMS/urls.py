"""OGMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404
from django.contrib.auth import views as auth_views

admin.site.site_header="Online Gas Booking"
admin.site.site_index="Welcome to Admin panel"
admin.site.site_title="vanraj"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('User.urls')),
    path('',include('core.urls')),
    path('user/reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('user/password_reset_sent/',auth_views.PasswordResetDoneView.as_view(),name = 'password_reset_done'),
    path('user/password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('user/reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler404 = 'User.views.error_404_view'