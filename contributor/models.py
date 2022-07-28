from django.db import models
from django.forms import CharField
from client.models import Client

# Create your models here.
class Contributor(Client):
    service_types=(
        ('Salaried','Salaried'),
        ('Self-employed','Self-employed'),
        ('Pensioner','Pensioner'),
        ('Family-pensioner','Family-pensioner'),
        ('Business','Business'),
        ('Farmer','Farmer'),
        ('Student','Student')

    )
    service_type = models.CharField(max_length=20,choices=service_types)
    

    def __str__(self):
        
        return super().__str__()
    

    