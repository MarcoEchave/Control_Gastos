from django.contrib import admin
from django.urls import path

from .views import (getCategoria,getTipo,DeleteBanco,DeleteCategoria,DeleteTipo,UpdateBanco,
                    UpdateCategoria,UpdateTipo,CreateBanco,CreateTipo)

from . import views

urlpatterns = [
    path('list-banco',views.getbanco,name='getBanco'),
    path('create-banco',CreateBanco.as_view(),name='createBanco'),
    path('update-banco/<pk>',UpdateBanco.as_view(),name='updateBanco'),
    path('delete-banco/<pk>',DeleteBanco.as_view(),name='deleteBanco'),
    path('get-categoria',views.getCategoria,name='getCategoria'),
    path('create-categoria',views.create_categoria,name='createCategoria'),
    path('update-categoria/<pk>',UpdateCategoria.as_view(),name='updateCategoria'),
    path('delete-categoria/<pk>',DeleteCategoria.as_view(),name='deleteCategoria'),
    path('list-tipo',views.getTipo,name='getTipo'),
    path('create-tipo',CreateTipo.as_view(),name='createTipo'),
    path('update-tipo/<pk>',UpdateTipo.as_view(),name='update-Tipo'),
    path('delete-tipo/<pk>',DeleteTipo.as_view(),name='delete-Tipo'),
]