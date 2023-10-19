from django.db import models

# Create your models here.
class Users(models.Model):
    nombre = models.CharField("Nombre",max_length=50)
    password = models.CharField("Password",max_length=30)