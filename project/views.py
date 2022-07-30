from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import Project
from project_contribution.models import ProjectContribution
from django.db.models import Sum
# Create your views here.
from django import template
register = template.Library()
class ProjectListView(ListView):
    model = Project
    template_name = "project/project_list.html"


    def get_context_data(self,*args, **kwargs):
        context = super(ProjectListView, self).get_context_data(*args,**kwargs)
        projects = context['object_list']
        funded_amounts =[]
        for project in projects:
            print(project.id)
            funded_amt = get_funded_amount(project.id)
            funded_amounts.append(funded_amt)
        context['funded_amounts']=funded_amounts
        return context

def get_funded_amount(project_id):
    contributions = ProjectContribution.objects.filter(project_id = project_id).all()
    amount = contributions.aggregate(funded = Sum('amount'))
    
    return amount['funded'] 


class ProjectDetailView(DetailView):
    model = Project
    template_name = "project/project_detail_view.html"

    def get_context_data(self,*args, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(*args,**kwargs)
        project_id = context['object'].id
        
        context['total_funded'] = get_funded_amount(project_id)
        
        return context


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