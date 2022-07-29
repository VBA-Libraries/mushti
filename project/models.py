from django.db import models
from main_user.models import MainUser

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    budget= models.DecimalField(max_digits=16, decimal_places=2)
    project_owner = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name