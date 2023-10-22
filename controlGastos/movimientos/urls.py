from django.contrib import admin
from django.urls import path,include

from .views import (getConcepto,getMovimiento,UpdateConcepto,DeleteConcepto,
                    UpdateMovimiento,DeleteMovimiento)

from . import views

urlpatterns = [
    path('get-concepto',views.getConcepto,name='getConcepto'),
    path('create-concepto',views.create_concepto,name='createConcepto'),
    path('update-concepto/<pk>',UpdateConcepto.as_view(),name='updateConcepto'),
    path('delete-concepto/<pk>',DeleteConcepto.as_view(),name='deleteConcepto'),
    path('get-movimientos',views.getMovimiento,name='getMovimientos'),
    path('create-movimientos',views.create_movimiento,name='createMovimientos'),
    path('update-movimientos/<pk>',UpdateMovimiento.as_view(),name='updateMovimientos'),
    path('delete-movimientos/<pk>',DeleteMovimiento.as_view(),name='deleteMovimientos'),
]