from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
# from django.utils.translation import ugettext_lazy as _
# from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField 


class CustomUserManager(BaseUserManager):


    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("Email should be provided")
        
        email=self.normalize_email(email)

        new_user = self.model(email=email,**extra_fields)
        new_user.set_password(password)
        new_user.save()

        return new_user

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True) 
        extra_fields.setdefault('is_superuser',True) 
        extra_fields.setdefault('is_active',True) 


        if extra_fields.get('is_staff') is not True:
            raise ValueError("super user should have is_staff as True")
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser should have is_superuser as True"))

        if extra_fields.get('is_active') is not True:
            raise ValueError('superuser should have is_active as True')

        return self.create_superuser(email,password,**extra_fields)

class User(AbstractUser):
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField(max_length=50,unique=True)
    phone_number = PhoneNumberField(null=False,unique=True)

    object = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone_number']

    def __str__(self) -> str:
        return f'User {self.email}'