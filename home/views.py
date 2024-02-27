from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.shortcuts import redirect
# Create your views here.

class LoginView(LoginView):
    template_name = 'home/login.html'

    def dispatch(self, request: HttpRequest, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('blog.list')
        return super().dispatch(request, *args, **kwargs)


class LogoutView(LogoutView):
    template_name = 'home/logout.html'

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'home/signup.html'
    success_url = '/blogs/'

    def dispatch(self, request: HttpRequest, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('blog.list')
        return super().dispatch(request, *args, **kwargs)

class Home(TemplateView):
    template_name = 'home/home.html'