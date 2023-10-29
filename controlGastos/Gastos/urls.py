from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('get-banco',views.getbanco,name='getBanco'),
    path('create-banco',views.create_banco,name='createBanco'),
    path('update-banco/<pk>',views.update_banco,name='updateBanco'),
    path('delete-banco/<pk>',views.eliminar_banco,name='deleteBanco'),
    path('get-categoria',views.getCategoria,name='getCategoria'),
    path('create-categoria',views.create_categoria,name='createCategoria'),
    path('update-categoria/<pk>',views.update_categoria,name='updateCategoria'),
    path('delete-categoria/<pk>',views.eliminar_categoria,name='deleteCategoria'),
    path('get-tipo',views.getTipo,name='getTipo'),
    path('create-tipo',views.create_tipo ,name='createTipo'),
    path('update-tipo/<pk>',views.update_tipo,name='update-Tipo'),
    path('delete-tipo/<pk>',views.eliminar_tipo,name='delete-Tipo'),
]