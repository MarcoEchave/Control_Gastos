from django import forms
from .models import Banco,Categoria,Tipo

class FormsBanco(forms.ModelForm):
    class Meta:
        model = Banco
        fields = ('banco',)


class FormsCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields =('categoria',)

class FormsTipo(forms.ModelForm):
    class Meta:
        model = Tipo
        fields =('tipo',)