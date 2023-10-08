from django.contrib import admin

# Register your models here.
from . models import Categoria, Banco,Tipo

admin.site.register(Categoria)
admin.site.register(Banco)
admin.site.register(Tipo)
