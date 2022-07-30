from django.db import models
from main_user.models import MainUser
from project.models import Project

# Create your models here.

class ProjectContribution(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE, related_name="entries")
    contributor = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=16,decimal_places=2)
    contribution_date = models.DateTimeField(auto_now_add=True)
    comments = models.TextField()

    def __str__(self) :
        return self.project.name + " " + str(self.amount)

    