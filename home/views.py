from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class LoginView(LoginView):
    template_name = 'home/login.html'

class LogoutView(LogoutView):
    template_name = 'home/logout.html'

