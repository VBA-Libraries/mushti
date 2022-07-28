from django.db import models

# Create your models here.
class Client(models.Model):
    genders = (('m','Male'),
    ('f','Female'))
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    contact_no = models.CharField(max_length=11)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=1,choices=genders)

    def __str__(self):
        return self.first_name + " " + self.last_name