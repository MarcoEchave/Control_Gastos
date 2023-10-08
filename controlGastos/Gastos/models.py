from django.db import models

# Create your models here
class Banco(models.Model):
    banco = models.CharField("Banco",max_length=30)

    def __str__(self):
        return self.banco
    
class Categoria(models.Model):
    categoria = models.CharField("Categoria",max_length=30)

    def __str__(self):
        return self.categoria
    
class Tipo(models.Model):
    tipo=models.CharField("Tipo",max_length=50)

    def __str__(self):
        return self.tipo
