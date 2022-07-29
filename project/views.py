from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project
# Create your views here.

class ProjectListView(ListView):
    model = Project
    template_name = "project/project_list.html"

class ProjectDetailView(DetailView):
    model = Project
    template_name = "project/project_detail_view.html"