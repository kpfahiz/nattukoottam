"""
URL configuration for nattukoottam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from donor.views import index, user_login, user_signup, user_logout, UserUpdateAPIView #user_register,

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='home'),
    path('signup/', user_signup, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    # path('user_registration/', user_register, name='userregister'),
    path('user_registration/', UserUpdateAPIView.as_view(), name='update'),

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
