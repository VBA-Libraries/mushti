from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

class MainBaseUserManager(BaseUserManager):

    def _create_user(self,email,password,first_name, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        user = self.model(email=email,first_name= first_name, **extra_fields)
        user.set_password (password)
        user.save()
        return user
    
    
    def create_user(self,email,password,first_name ,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',False)
        
        self._create_user(email,password, first_name=first_name, **extra_fields)
    
    def create_superuser(self,email,password,first_name=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',True)
        self._create_user(email,password, first_name=first_name, **extra_fields)




class MainUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200,null=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    genders = (('m','Male'),
    ('f','Female'))
    last_name = models.CharField(max_length=100, null=True)
    address = models.TextField(null=True)
    contact_no = models.CharField(max_length=11,null=True)
    
    gender = models.CharField(max_length=1,choices=genders,null=True)

    USERNAME_FIELD = 'email'
    objects = MainBaseUserManager()
    def full_name(self):
        return self.first_name
    def has_module_perms(self,app_label):
        return self.is_superuser
    def has_perm(self,app_label):
        return self.is_superuser