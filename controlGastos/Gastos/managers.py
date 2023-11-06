from django.db import models


class BancoManagers(models.Manager):

    def buscar_banco(self, kword):
        resultado = self.filter(banco__icontains=kword)
        return resultado
    

class CategoriaManagers(models.Manager):
    
    def buscar_categoria(self, kword):
        resultado = self.filter(categoria__icontains=kword)
        return resultado
    
class TipoaManagers(models.Manager):
    
    def buscar_tipo(self, kword):
        resultado = self.filter(tipo__icontains=kword)
        return resultado