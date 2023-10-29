from django.shortcuts import render,get_object_or_404
from django.views.generic import(UpdateView,DeleteView)
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Concepto, Movimiento
from .forms import FormConcepto, FormMovimiento

# Create your views here.
@login_required
def getConcepto(request):
    concepto = Concepto.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(concepto,5)
    concepto = paginator.page(page)
    return render(request,'concepto/getConcepto.html',{'concepto':concepto,'paginator':paginator})

@login_required    
def create_concepto(request):
    if request.method == 'POST':
        form = FormConcepto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('getConcepto')
    else:
        form = FormConcepto()
    return render(request, 'concepto/create-concepto.html', {'form': form})


@login_required
def update_concepto(request, pk):
    concepto = get_object_or_404(Concepto, pk=pk)
    if request.method == 'POST':
        form = FormConcepto(request.POST, instance=concepto)
        if form.is_valid():
            form.save()
            return redirect('getConcepto')
    else:
        form = FormConcepto(instance=concepto)
    return render(request, 'concepto/update-concepto.html', {'form': form, 'concepto': concepto})

@login_required
def eliminar_concepto(request, pk):
    concepto = get_object_or_404(Concepto, pk=pk)
    if request.method == 'POST':
        concepto.delete()
        return redirect('getConcepto')
    return render(request, 'concepto/delete-concepto.html', {'concepto': concepto})
#Movimiento

@login_required
def getMovimiento(request):
    movimiento = Movimiento.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(movimiento,5)
    movimiento = paginator.page(page)
    return render(request,'movimientos/get-movimientos.html',{'movimiento':movimiento,'paginator':paginator})

@login_required    
def create_movimiento(request):
    if request.method == 'POST':
        form = FormMovimiento(request.POST)
        if form.is_valid():
            form.save()
            return redirect('getMovimientos')
    else:
        form = FormMovimiento()
    return render(request, 'movimientos/create-movimiento.html', {'form': form})

@login_required
def update_movimiento(request, pk):
    movimiento = get_object_or_404(Movimiento, pk=pk)
    if request.method == 'POST':
        form = FormMovimiento(request.POST, instance=movimiento)
        if form.is_valid():
            form.save()
            return redirect('getMovimiento')
    else:
        form = FormConcepto(instance=movimiento)
    return render(request, 'movimiento/update-movimiento.html', {'form': form, 'movimiento': movimiento})

@login_required
def eliminar_movimiento(request, pk):
    movimimiento = get_object_or_404(Movimiento, pk=pk)
    if request.method == 'POST':
        movimimiento.delete()
        return redirect('getMovimientos')
    return render(request, 'movimientos/delete-movimiento.html', {'movimiento': movimimiento})