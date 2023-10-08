from django.db import models

# Create your models here.

from Gastos.models import Categoria,Banco,Tipo

class Concepto(models.Model):
    concepto = models.CharField("Concepto",max_length=50)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.concepto


class Movimiento(models.Model):
    fecha=models.DateTimeField("Fecha", blank=True, null=True)
    id_concepto=models.ForeignKey(Concepto,on_delete=models.CASCADE)
    monto=models.DecimalField("Monto",max_digits=6,decimal_places=2)
    banco=models.ForeignKey(Banco,on_delete=models.CASCADE)
    tipo= models.ForeignKey(Tipo,on_delete=models.CASCADE)

    def __str__(self):
        return self.fecha+"-"+self.id_concepto+"-"+self.monto+"-"+self.tipo