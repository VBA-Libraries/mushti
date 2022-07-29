from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

class MainBaseUserManager(BaseUserManager):

    def _create_user(self,email,password, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        user = self.model(email=email, **extra_fields)
        user.set_password (password)
        user.save()
        return user
    
    
    def create_user(self,email,password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',False)
        self._create_user(email,password,**extra_fields)
    
    def create_superuser(self,email,password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',True)
        self._create_user(email,password,**extra_fields)




class MainUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)



    USERNAME_FIELD = 'email'
    objects = MainBaseUserManager()
    def full_name(self):

        return "Bhanu Sinha"
    def has_module_perms(self,app_label):
        return self.is_superuser
    def has_perm(self,app_label):
        return self.is_superuser