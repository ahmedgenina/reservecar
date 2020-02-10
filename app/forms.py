# -*- coding: utf-8 -*-
from django import forms
from .models import Veiculo, Motorista, Reserva


class FormMotorista(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = ['nome', 'cpf', 'telefone', 'sexo']
        widgets ={
            'nome': forms.TextInput(attrs={'class': 'form-control', 'maxlenght': 100}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'maxlenght': 11}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'maxlenght': 20}),
            'sexo': forms.Select(attrs={'class': 'form-control', 'maxlenght': 10}, choices=model.SEXO_CHOICES),
        }


class FormVeiculo(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['modelo', 'placa', 'ano', 'estado', 'foto_veiculo']
        widgets ={
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'maxlenght': 50}),
            'placa': forms.TextInput(attrs={'class': 'form-control', 'maxlenght': 8}),
            'ano': forms.TextInput(attrs={'class': 'form-control', 'maxlenght': 4}),
            'estado': forms.Select(attrs={'class': 'form-control', 'maxlenght': 10}, choices=model.ESTADO_CHOICES),
            'foto_veiculo': forms.FileInput()
        }


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M"
        super().__init__(**kwargs)


class FormReserva(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['data_inicio', 'data_final', 'veiculo', 'motorista']
        widgets ={
            'data_inicio': DateTimeInput(),
            'data_final': DateTimeInput(),
            'veiculo': forms.Select(attrs={'class': 'form-control', 'maxlenght': 50}, choices=model.objects.all()),
            'motorista': forms.Select(attrs={'class': 'form-control', 'maxlenght': 50}, choices=model.objects.all()),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["data_inicio"].input_formats = ["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"]
        self.fields["data_final"].input_formats = ["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"]