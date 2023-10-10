from django import forms

from .model import Movimiento, Concepto


class FormMovimiento(forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = ('fecha',"concepto","monto","banco")
        widgets = {"monto":from.NumberInput(),"fecha":forms.DateInput()}


class FormConcepto(forms.ModelForm):
    model=Concepto
    fields =("concepto","categoria")
    