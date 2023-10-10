from django.contrib import admin
from django.urls import path,include

from .views import (getConcepto,getMovimiento,CreateConcepto,UpdateConcepto,DeleteConcepto,
                    CreateMovimiento,UpdateMovimiento,DeleteMovimiento)

urlpatterns = [
    path('get-concepto',getConcepto.as_view(),name=''),
    path('create-concepto',CreateConcepto.as_view(),name=''),
    path('update-concepto/<pk>',UpdateConcepto.as_view(),name=''),
    path('delete-concepto/<pk>',DeleteConcepto.as_view(),name=''),
    path('get-movimientos',getMovimiento.as_view(),name=''),
    path('create-movimientos',CreateMovimiento.as_view(),name=''),
    path('update-movimientos/<pk>',UpdateMovimiento.as_view(),name=''),
    path('delete-movimientos/<pk>',DeleteMovimiento.as_view(),name=''),
]