from django.contrib import admin
from django.urls import path

from .views import (getBanco,getCategoria,getTipo,DeleteBanco,DeleteCategoria,DeleteTipo,UpdateBanco,
                    UpdateCategoria,UpdateTipo,CreateBanco,CreateCategoria,CreateTipo)

urlpatterns = [
    path('list-banco',getBanco.as_view(),name='getBanco'),
    path('create-banco',CreateBanco.as_view(),name='createBanco'),
    path('update-banco/<pk>',UpdateBanco.as_view(),name='updateBanco'),
    path('delete-banco/<pk>',DeleteBanco.as_view(),name='deleteBanco'),
    path('get-categoria',getCategoria.as_view(),name='getCategoria'),
    path('create-categoria',CreateCategoria.as_view(),name='createCategoria'),
    path('update-categoria/<pk>',UpdateCategoria.as_view(),name='updateCategoria'),
    path('delete-categoria/<pk>',DeleteCategoria.as_view(),name='deleteCategoria'),
    path('list-tipo',getTipo.as_view(),name='listTipo'),
    path('create-tipo',CreateTipo.as_view(),name='createTipo'),
    path('update-tipo/<pk>',UpdateTipo.as_view(),name='update-Tipo'),
    path('delete-tipo/<pk>',DeleteTipo.as_view(),name='delete-Tipo'),
]