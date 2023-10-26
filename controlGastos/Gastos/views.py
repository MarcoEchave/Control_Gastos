from typing import Any
from django.shortcuts import render,redirect
from django.views.generic import (UpdateView,DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Banco,Tipo,Categoria

from .forms import FormsCategoria,FormsTipo,FormsBanco

# Create your views here.
@login_required
#@permission_required('')
def getbanco(request):
    banco = Banco.objects.all()
    return render(request,'banco/getBanco.html',{'banco':banco})

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

class UpdateBanco(LoginRequiredMixin,UpdateView):
    template_name='banco/update-banco.html'
    model = Banco
    fields = ['banco']
    success_url = reverse_lazy("getCategoria")
    login_url = reverse_lazy("user-login")

class DeleteBanco(LoginRequiredMixin,DeleteView):
    template_name='banco/delete-banco.html'
    model=Banco
    success_url = reverse_lazy('getBanco')

##Tipo
@login_required 
def getTipo(request):
    tipo = Tipo.objects.all()
    return render(request,'tipo/getTipo.html',{'tipo':tipo})
    
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

class UpdateTipo(LoginRequiredMixin,UpdateView):
    template_name='tipo/update-tipo.html'
    model = Tipo
    fields = ['tipo']
    success_url = reverse_lazy("getCategoria")

class DeleteTipo(LoginRequiredMixin,DeleteView):
    template_name='tipo/delete-tipo.html'
    model = Tipo
    success_url = reverse_lazy('getTipo')

#Categoria
@login_required
def getCategoria(request):
    categoria= Categoria.objects.all()
    return render(request,'categoria/getCategoria.html',{'categoria':categoria})

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
    
class UpdateCategoria(LoginRequiredMixin,UpdateView):
    template_name='categoria/update-categoria.html'
    model = Categoria
    fields = ['categoria']
    success_url = reverse_lazy("getCategoria")

class DeleteCategoria(LoginRequiredMixin,DeleteView):
    template_name='categoria/delete-categoria.html'
    model = Categoria
    success_url = reverse_lazy('getCategoria')
