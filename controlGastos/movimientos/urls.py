from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('get-concepto',views.getConcepto,name='getConcepto'),
    path('create-concepto',views.create_concepto,name='createConcepto'),
    path('update-concepto/<pk>',views.update_concepto,name='updateConcepto'),
    path('delete-concepto/<pk>',views.eliminar_concepto,name='deleteConcepto'),
    path('get-movimientos',views.getMovimiento,name='getMovimientos'),
    path('create-movimientos',views.create_movimiento,name='createMovimientos'),
    path('update-movimientos/<pk>',views.update_movimiento,name='updateMovimientos'),
    path('delete-movimientos/<pk>',views.eliminar_movimiento,name='deleteMovimientos'),
    
]