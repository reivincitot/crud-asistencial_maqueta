from django.shortcuts import render
from rest_framework import viewsets
from .serializerz import RegionsSerializer, ProvinceSerializers, CommuneSerializers, AddressSerializers
from .models import Regions, Province, Commune, Address


class RegionsViewSets(viewsets.ModelViewSet):
    """
    API endpoint para el registro de las Regiones
    """
    queryset= Regions.objects.all()
    serializer_class = RegionsSerializer

class ProvinceViewSets(viewsets.ModelViewSet):
    """
    API endpoint para el registro de las Provincias
    """
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializers

class CommuneViewSets(viewsets.ModelViewSet):
    """
    API endpoint para el registro de las Comunas
    """
    queryset = Commune.objects.all()
    serializer_class = CommuneSerializers

class AddressViewSets(viewsets.ModelViewSet):
    """
    API para el registro de las Direcciones
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializers