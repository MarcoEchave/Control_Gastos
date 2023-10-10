from django.shortcuts import render
from django.views.generic import(ListView)

from .models import Concepto, Movimiento

# Create your views here.
class getConcepto(ListView):
    template_name= 'concepto/getConcepto.html'
    model =Concepto
    context_object_name = 'concepto'

class CreateConcepto(ListView):
    template_name= 'concepto/CreateConcepto.html'
    model =Concepto
    context_object_name = 'concepto'

class UpdateConcepto(ListView):
    template_name= 'concepto/updateConcepto.html'
    model =Concepto
    context_object_name = 'concepto'

class DeleteConcepto(ListView):
    template_name= 'concepto/deleteConcepto.html'
    model =Concepto
    context_object_name = 'concepto'

class getMovimiento(ListView):
    template_name = 'movimiento/getMovimiento.html'
    model= Movimiento
    context_object_name='movimiento'


class CreateMovimiento(ListView):
    template_name = 'movimiento/CreateMovimiento.html'
    model= Movimiento
    context_object_name='movimiento'


class UpdateMovimiento(ListView):
    template_name = 'movimiento/UpdateMovimiento.html'
    model= Movimiento
    context_object_name='movimiento'

class DeleteMovimiento(ListView):
    template_name = 'movimiento/DeleteMovimiento.html'
    model= Movimiento
    context_object_name='movimiento'