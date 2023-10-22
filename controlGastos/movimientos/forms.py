from django import forms

from .models import Movimiento, Concepto


class FormMovimiento(forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = ('fecha',"id_concepto","monto","banco","tipo")
        widgets = {"monto":forms.NumberInput(),"fecha":forms.DateInput()}


class FormConcepto(forms.ModelForm):
    class Meta:
        model=Concepto
        fields =("concepto","id_categoria")
    