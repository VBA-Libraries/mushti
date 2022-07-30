from dataclasses import fields
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import CreateView
from django import forms
from project.models import Project

from .models import ProjectContribution

# Create your views here.

class ProjectContributionCreateView(CreateView):
    model = ProjectContribution
    template_name = "project_contribution/project_contribution_create_view.html"
    fields=['amount']

class ProjectContributionForm(forms.ModelForm):
    
    class Meta:
        
        model= ProjectContribution
        fields=['amount']


def project_contribution_create_view(request):
    form = ProjectContributionForm(request.POST or None)
    context={}
    if request.method == "POST":
    
        amount = request.POST.get('amount')
        print(amount)
        if form.is_valid():
            project_id = request.POST.get('project_id')
            obj = form.save(commit=False)
            project = Project.objects.get(pk=project_id)
            obj.project = project
            obj.contributor = request.user
            obj.save()
        else:
            raise ValueError("Invalid form")
    else:
        raise ValueError("Invalid")

    context['object']= project

    return render (request, 'project_contribution/success.html',context)


