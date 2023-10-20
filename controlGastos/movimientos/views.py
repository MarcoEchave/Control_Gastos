from django.shortcuts import render
from django.views.generic import(ListView)
from django.urls import reverse_lazy

from .models import Concepto, Movimiento
from .forms import FormConcepto, FormMovimiento

# Create your views here.
def getConcepto(request):
    concepto = Concepto.objects.all()
    return render(request,'concepto/getConcepto.html',{'concepto':concepto})
    
def create_concepto(request):
    if request.method == 'POST':
        form = FormConcepto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('getConcepto')
    else:
        form = FormsBanco()
    return render(request, 'concepto/create-concepto.html', {'form': form})

class UpdateConcepto(ListView):
    template_name= 'concepto/updateConcepto.html'
    model =Concepto
    context_object_name = 'concepto'

class DeleteConcepto(ListView):
    template_name= 'concepto/deleteConcepto.html'
    model =Concepto
    success_url = reverse_lazy('getConcepto')
#Movimiento
def getConcepto(request):
    movimiento = Movimiento.objects.all()
    return render(request,'movimiento/getMovimiento.html',{'movimiento':movimiento})
    
def create_concepto(request):
    if request.method == 'POST':
        form = FormMovimiento(request.POST)
        if form.is_valid():
            form.save()
            return redirect('getMovimientos')
    else:
        form = FormsBanco()
    return render(request, 'movimiento/create-movimiento.html', {'form': form})

class UpdateMovimiento(ListView):
    template_name = 'movimiento/UpdateMovimiento.html'
    model= Movimiento
    context_object_name='movimiento'

class DeleteMovimiento(ListView):
    template_name = 'movimiento/delete-movimiento.html'
    model= Movimiento
    success_url = reverse_lazy('getMovimiento')