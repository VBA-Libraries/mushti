from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import Project
# Create your views here.

class ProjectListView(ListView):
    model = Project
    template_name = "project/project_list.html"

class ProjectDetailView(DetailView):
    model = Project
    template_name = "project/project_detail_view.html"

class ProjectCreateView(CreateView):
    model = Project
    template_name = "project/project_create_view.html"
    fields=['name','description','budget']

    def get_success_url(self):
        return reverse('project_list_view')

    def form_valid(self, form) :
        project = form.instance
        project.project_owner = self.request.user
        
        return super().form_valid(form)