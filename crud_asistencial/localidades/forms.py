# forms.py
from django import forms
from .models import Pais, Region, Provincia, Comuna, Ciudad
from utils import verificar_duplicado

class LocalidadesForm(forms.Form):
    nuevoPais = forms.CharField(required=False)
    nuevoCodigoPais = forms.CharField(required=False)
    nuevaRegion = forms.CharField(required=False)
    nuevoCodigoRegion = forms.CharField(required=False)
    nuevaProvincia = forms.CharField(required=False)
    nuevaComuna = forms.CharField(required=False)
    nuevaCiudad = forms.CharField(required=False)

    def clean_nuevoPais(self):
        nuevoPais = self.cleaned_data.get('nuevoPais')
        if nuevoPais:
            verificar_duplicado(Pais, 'nombre', nuevoPais)
        return nuevoPais

    def clean_nuevoCodigoPais(self):
        nuevoCodigoPais = self.cleaned_data.get('nuevoCodigoPais')
        if nuevoCodigoPais:
            verificar_duplicado(Pais, 'codigo', nuevoCodigoPais)
        return nuevoCodigoPais

    def clean_nuevaRegion(self):
        nuevaRegion = self.cleaned_data.get('nuevaRegion')
        if nuevaRegion:
            verificar_duplicado(Region, 'nombre', nuevaRegion)
        return nuevaRegion

    def clean_nuevoCodigoRegion(self):
        nuevoCodigoRegion = self.cleaned_data.get('nuevoCodigoRegion')
        if nuevoCodigoRegion:
            verificar_duplicado(Region, 'codigo', nuevoCodigoRegion)
        return nuevoCodigoRegion

    def clean_nuevaProvincia(self):
        nuevaProvincia = self.cleaned_data.get('nuevaProvincia')
        if nuevaProvincia:
            verificar_duplicado(Provincia, 'nombre', nuevaProvincia)
        return nuevaProvincia

    def clean_nuevaComuna(self):
        nuevaComuna = self.cleaned_data.get('nuevaComuna')
        if nuevaComuna:
            verificar_duplicado(Comuna, 'nombre', nuevaComuna)
        return nuevaComuna

    def clean_nuevaCiudad(self):
        nuevaCiudad = self.cleaned_data.get('nuevaCiudad')
        if nuevaCiudad:
            verificar_duplicado(Ciudad, 'nombre', nuevaCiudad)
        return nuevaCiudad
