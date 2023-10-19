from typing import Any
from django.shortcuts import render,redirect
from django.db.models.query import QuerySet
from django.views.generic import (ListView,DetailView,CreateView,TemplateView,UpdateView,DeleteView)

from .models import Banco,Tipo,Categoria

from .forms import FormsCategoria

# Create your views here.

def getbanco(request):
    banco = Banco.objects.all()
    return render(request,'banco/getBanco.html',{'banco':banco})
    
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
def getTipo(request):
    tipo = Tipo.objects.all()
    return render(request,'tipo/getTipo.html',{'tipo':tipo})
    
    
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
def getCategoria(request):
    categoria= Categoria.objects.all()
    return render(request,'categoria/getCategoria.html',{'categoria':categoria})

def create_categoria(request):
    if request.method == 'POST':
        form = FormsCategoria(request.POST)
        if form.is_valid():
            form.save()
            return redirect('getCategoria')
    else:
        form = FormsCategoria()
    return render(request, 'categoria/create-categoria.html', {'form': form})
    
class UpdateCategoria(UpdateView):
    template_name='categoria/updateCategoria.html'
    context_object_name='updateCategoria'

class DeleteCategoria(DeleteView):
    template_name='categoria/deleteCategoria.html'
    context_object_name='deletecategoria'