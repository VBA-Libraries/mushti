from django.db import models
from contributor.models import Contributor
from project.models import Project

# Create your models here.

class ProjectContribution(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=16,decimal_places=2)
    contribution_date = models.DateTimeField(auto_now_add=True)
    comments = models.TextField()
    