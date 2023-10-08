from django.contrib import admin

# Register your models here.
from .models import Movimiento,Concepto

admin.site.register(Movimiento)
admin.site.register(Concepto)