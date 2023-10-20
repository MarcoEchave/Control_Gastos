from typing import Any
from django.shortcuts import render,redirect
from django.db.models.query import QuerySet
from django.views.generic import (UpdateView,DeleteView)
from django.urls import reverse_lazy

from .models import Banco,Tipo,Categoria

from .forms import FormsCategoria,FormsTipo,FormsBanco

# Create your views here.

def getbanco(request):
    banco = Banco.objects.all()
    return render(request,'banco/getBanco.html',{'banco':banco})
    
def create_banco(request):
    if request.method == 'POST':
        form = FormsBanco(request.POST)
        if form.is_valid():
            form.save()
            return redirect('getBanco')
    else:
        form = FormsBanco()
    return render(request, 'banco/create-banco.html', {'form': form})

class UpdateBanco(UpdateView):
    template_name='banco/updateBanco.html'
    context_object_name='updateBanco'

class DeleteBanco(DeleteView):
    template_name='banco/deleteBanco.html'
    context_object_name='deleteBanco'
    success_url = reverse_lazy('getBanco')

##Tipo
def getTipo(request):
    tipo = Tipo.objects.all()
    return render(request,'tipo/getTipo.html',{'tipo':tipo})
    
    
def create_tipo(request):
    if request.method == 'POST':
        form = FormsTipo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createTipo')
    else:
        form = FormsTipo()
    return render(request, 'tipo/create-tipo.html', {'form': form})

class UpdateTipo(UpdateView):
    template_name='tipo/updateTipo.html'
    context_object_name='updateTipo'

class DeleteTipo(DeleteView):
    template_name='tipo/deleteTipo.html'
    context_object_name='deleteTipo'
    model = Tipo
    success_url = reverse_lazy('getTipo')

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
    model = Categoria
    success_url = reverse_lazy('getCategoria')
