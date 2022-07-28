from turtle import update
import django
from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView
from .models import Contributor 
from django.urls import reverse

# Create your views here.
class CreateContributorView(CreateView):
    model = Contributor
    template_name= 'contributor/contributor_create_view.html'
    fields= ['first_name','last_name','address','contact_no','email','gender','service_type']

    def get_success_url(self):
        return reverse('list_contributor')


class ContributorListView(ListView):
    model = Contributor
    template_name= 'contributor/contributor_list_view.html'


    # def get_success_url(self):
    #     return reverse

class ContributorUpdateView(UpdateView):
    model = Contributor
    template_name= 'contributor/contributor_create_view.html'
    fields= ['first_name','last_name','address','contact_no','email','gender','service_type']

    def get_success_url(self):
        return reverse('list_contributor')
    

