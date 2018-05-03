"""CrudUser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from apps.user import views as au
from django.contrib.auth.views import login

urlpatterns = [
    #Ignorar
    #-------------------------------------------------------#
    path('admin/', admin.site.urls),
    path('user/nuevo', au.UserCreate.as_view(),name='user_view'),
    path('user/listar', au.UserList.as_view(),name='user_list'),
    path('user/edit/<int:pk>', au.UserUpdate.as_view(),name='user_edit'),
    path('user/delete/<int:pk>', au.UserDelete.as_view(),name='user_delete'),
    #-------------------------------------------------------#
    #API
    path('user/apilist', au.UserAPIList.as_view(),name='user_apilist'),
    path('user/apiupdate/<int:pk>', au.UserAPIUpdate.as_view(),name='user_apiupdate'),
]
