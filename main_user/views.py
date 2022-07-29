from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .models import MainUser

# Create your views here.

class UserLoginView(LoginView):
    template_name = "account/login.html"

    
   

    def get_success_url(self):
        return reverse('project_list_view')
        

class UserLogoutView(LogoutView):
    template_name = "account/logout.html"
    

class UserCreateView(CreateView):
    model = MainUser
    template_name = "account/signup.html"
    fields = ['email','password','first_name']
    
    def form_valid(self, form):
        user = form.instance
        user.set_password (form.instance.password)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('login_view')
        

class UserCreateFullView(CreateView):
    model = MainUser
    template_name = "account/signup.html"
    fields = ['email','password','first_name']
    
    def form_valid(self, form):
        user = form.instance
        user.set_password (form.instance.password)
        return super().form_valid(form)