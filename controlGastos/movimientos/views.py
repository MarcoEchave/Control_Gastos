from django.shortcuts import render
from django.views.generic import(ListView,DeleteView)
from django.urls import reverse_lazy
from django.shortcuts import redirect

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
        form = FormConcepto()
    return render(request, 'concepto/create-concepto.html', {'form': form})

class UpdateConcepto(ListView):
    template_name= 'concepto/updateConcepto.html'
    model =Concepto
    context_object_name = 'concepto'

class DeleteConcepto(DeleteView):
    template_name= 'concepto/delete-concepto.html'
    model =Concepto
    success_url = reverse_lazy('getConcepto')
#Movimiento
def getMovimiento(request):
    movimiento = Movimiento.objects.all()
    return render(request,'movimientos/get-movimientos.html',{'movimiento':movimiento})
    
def create_movimiento(request):
    if request.method == 'POST':
        form = FormMovimiento(request.POST)
        if form.is_valid():
            form.save()
            return redirect('getMovimientos')
    else:
        form = FormMovimiento()
    return render(request, 'movimientos/create-movimiento.html', {'form': form})

class UpdateMovimiento(ListView):
    template_name = 'movimientos/UpdateMovimiento.html'
    model= Movimiento
    context_object_name='movimiento'

class DeleteMovimiento(DeleteView):
    template_name = 'movimientos/delete-movimiento.html'
    model= Movimiento
    success_url = reverse_lazy('getMovimientos')