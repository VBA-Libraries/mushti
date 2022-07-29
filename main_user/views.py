from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .models import MainUser

# Create your views here.

class UserLoginView(LoginView):
    template_name = "account/login.html"

class UserLogoutView(LogoutView):
    template_name = "account/logout.html"
    

class UserCreateView(CreateView):
    model = MainUser
    template_name = "account/signup.html"
    fields = ['email','password']
    
    def form_valid(self, form):
        user = form.instance
        user.set_password (form.instance.password)
        return super().form_valid(form)