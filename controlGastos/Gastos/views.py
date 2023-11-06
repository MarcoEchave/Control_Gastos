from typing import Any
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Banco,Tipo,Categoria
from .managers import CategoriaManagers,BancoManagers,TipoaManagers
from .forms import FormsCategoria,FormsTipo,FormsBanco

# Create your views here.
@login_required
#@permission_required('')
def getbanco(request):
    banco = Banco.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(banco,5)
    banco = paginator.page(page)
    return render(request,'banco/getBanco.html',{'banco':banco,'paginator':paginator})

@login_required   
def create_banco(request):
    if request.method == 'POST':
        form = FormsBanco(request.POST)
        if form.is_valid():
            form.save()
            return redirect('getBanco')
    else:
        form = FormsBanco()
    return render(request, 'banco/create-banco.html', {'form': form})

@login_required
def update_banco(request, pk):
    banco = get_object_or_404(Banco, pk=pk)
    if request.method == 'POST':
        form = FormsBanco(request.POST, instance=banco)
        if form.is_valid():
            form.save()
            return redirect('getBanco')
    else:
        form = FormsBanco(instance=banco)
    return render(request, 'banco/update-banco.html', {'form': form, 'banco': banco})

@login_required
def eliminar_banco(request, pk):
    banco = get_object_or_404(Banco, pk=pk)
    if request.method == 'POST':
        banco.delete()
        return redirect('getBanco')
    return render(request, 'banco/delete-banco.html', {'banco': banco})

##Tipo
@login_required 
def getTipo(request):
    tipo = Tipo.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(tipo,5)
    tipo = paginator.page(page)
    return render(request,'tipo/getTipo.html',{'tipo':tipo,'paginator':paginator})
    
@login_required  
def create_tipo(request):
    if request.method == 'POST':
        form = FormsTipo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('getTipo')
    else:
        form = FormsTipo()
    return render(request, 'tipo/create-tipo.html', {'form': form})

@login_required
def update_tipo(request, pk):
    tipo = get_object_or_404(Tipo, pk=pk)
    if request.method == 'POST':
        form = FormsTipo(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect('getTipo')
    else:
        form = FormsTipo(instance=tipo)
    return render(request, 'tipo/update-tipo.html', {'form': form, 'tipo': tipo})

@login_required
def eliminar_tipo(request, pk):
    tipo = get_object_or_404(Tipo, pk=pk)
    if request.method == 'POST':
        tipo.delete()
        return redirect('getTipo')
    return render(request, 'tipo/delete-tipo.html', {'tipo': tipo})

#Categoria
@login_required
def getCategoria(request):
    categoria= Categoria.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(categoria,5)
    categoria = paginator.page(page)
    return render(request,'categoria/getCategoria.html',{'categoria':categoria,'paginator':paginator})

@login_required
def create_categoria(request):
    if request.method == 'POST':
        form = FormsCategoria(request.POST)
        if form.is_valid():
            form.save()
            return redirect('getCategoria')
    else:
        form = FormsCategoria()
    return render(request, 'categoria/create-categoria.html', {'form': form})
    
@login_required
def update_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = FormsCategoria(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('getCategoria')
    else:
        form = FormsCategoria(instance=categoria)
    return render(request, 'categoria/update-categoria.html', {'form': form, 'categoria': categoria})

@login_required
def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('getCategoria')
    return render(request, 'categoria/delete-categoria.html', {'categoria': categoria})

@login_required
def filtrar_categoria(request, self):
    palabra = self.request.GET.get("kword","")
    filtro =CategoriaManagers.buscar_categoria(palabra)
    return render(request,'categoria/filtro-categoria.html',{'filtro':filtro} )
