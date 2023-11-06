from django.db import models
from django.db.models import Sum


class ConceptoManagers(models.Manager):
    
    def buscar_concepto(self, kword):
        resultado = self.filter(concepto__icontains=kword)
        return resultado
    

class MovimientoManagers(models.Manager):
    
    def buscar_movimiento(self, kword):
        resultado = self.filter(movimiento__icontains=kword)
        return resultado
    

    def suma_movimientos(self):
        suma = self.aaggregate(Sum("monto"))
        print (suma)
        return suma
