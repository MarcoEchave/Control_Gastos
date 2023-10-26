from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

# Create your models here.
class Users(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    nombre = models.CharField("Nombre",max_length=50)
    password = models.CharField("Password",max_length=100)
    email = models.EmailField(default="a@dominio.com")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    def get_short_name(self):
        return self.username
    