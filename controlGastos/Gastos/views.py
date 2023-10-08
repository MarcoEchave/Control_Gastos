from typing import Any
from django.shortcuts import render
from django.db.models.query import QuerySet
from django.views.generic import (ListView,DetailView,CreateView,TemplateView,UpdateView,DeleteView)

from .models import Banco,Tipo,Categoria

# Create your views here.

class getBanco(ListView):
    template_name = 'banco/getBanco.html'
    model = Banco
    context_object_name = 'banco'
    paginate_by=2

    #def get_queryset(self):
    #    palabra_clave = self.request.GET.get("kword", '')
    #    lista = Banco.objects.get(id=1)       
    #    return lista
    
class CreateBanco(CreateView):
    template_name='banco/createBanco.html'
    context_object_name='createBanco'

class UpdateBanco(UpdateView):
    template_name='banco/updateBanco.html'
    context_object_name='updateBanco'

class DeleteBanco(DeleteView):
    template_name='banco/deleteBanco.html'
    context_object_name='deleteBanco'

##Tipo
class getTipo(ListView):
    template_name = 'tipo/getTipo.html'
    context_object_name = 'tipo'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Banco.objects.get(id=1)       
        return lista
    
class CreateTipo(CreateView):
    template_name='tipo/createTipo.html'
    context_object_name='createTipo'

class UpdateTipo(UpdateView):
    template_name='tipo/updateTipo.html'
    context_object_name='updateTipo'

class DeleteTipo(DeleteView):
    template_name='tipo/deleteTipo.html'
    context_object_name='deleteTipo'

#Categoria
class getCategoria(ListView):
    template_name = 'categoria/getCategoria.html'
    context_object_name = 'categoria'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Banco.objects.get(id=1)       
        return lista
    
class CreateCategoria(CreateView):
    template_name='categoria/createCategoria.html'
    context_object_name='createCategoria'

class UpdateCategoria(UpdateView):
    template_name='categoria/updateCategoria.html'
    context_object_name='updateCategoria'

class DeleteCategoria(DeleteView):
    template_name='categoria/deleteCategoria.html'
    context_object_name='deletecategoria'