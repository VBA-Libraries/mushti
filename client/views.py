
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from .models import Client
from django.urls import reverse

# Create your views here.

class CreateClientView(CreateView):
    model=Client
    template_name= 'clients/client_create_view.html'
    # fields = Client._meta.get_fields()
    fields = ['first_name','last_name','address','contact_no','email','gender']

    def get_success_url(self):
        return reverse('list_client')



class ClientListView(ListView):
    model = Client
    template_name= 'clients/client_list_view.html'


    # def get_success_url(self):
    #     return reverse

class ClientUpdateView(UpdateView):
    model = Client
    template_name= 'clients/client_create_view.html'
    fields = ['first_name','last_name','address','contact_no','email','gender']

    def get_success_url(self):
        return reverse('list_client')
    