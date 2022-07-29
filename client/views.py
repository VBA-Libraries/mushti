
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Client
from django.urls import reverse

# Create your views here.

class CreateClientView(CreateView):
    model=Client
    template_name= "clients/client_create_view.html"
    # fields = Client._meta.get_fields()
    fields = ['first_name','last_name','address','contact_no','email','gender']

    def get_success_url(self):
        return reverse('add_client')