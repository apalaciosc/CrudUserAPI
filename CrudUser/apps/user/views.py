from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from apps.user.forms import UserForm
from apps.user.models import User

from rest_framework import generics,permissions
from rest_framework.views import APIView
from apps.user.serializers import UserSerializer
import json

# Create your views here.
class UserAPIList(generics.ListCreateAPIView):
    queryset=User.objects.all()
    permission_classes=(permissions.IsAuthenticated,)
    serializer_class=UserSerializer


class UserAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    permission_classes=(permissions.IsAuthenticated,)
    serializer_class = UserSerializer













class UserList(ListView):
    model=User
    template_name='user_list.html'
    paginate_by=2

class UserCreate(CreateView):
    model=User
    form_class=UserForm
    template_name='user_form.html'
    success_url=reverse_lazy('user_list')

class UserUpdate(UpdateView):
    model=User
    form_class=UserForm
    template_name='user_form.html'
    success_url=reverse_lazy('user_list')

class UserDelete(DeleteView):
    model=User
    template_name='user_delete.html'
    success_url=reverse_lazy('user_list')
