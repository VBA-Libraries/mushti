import django
from django.shortcuts import render
from django.views.generic import CreateView,ListView
from .models import Contributor
from django.urls import reverse

# Create your views here.
class CreateContributorView(CreateView):
    model = Contributor
    template_name= 'contributor/create_view.html'
    fields= ['first_name','last_name','address','contact_no','email','gender','service_type']

    def get_success_url(self):
        return reverse('add_contributor')

