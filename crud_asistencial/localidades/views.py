from django.shortcuts import render, get_object_or_404
from .models import Pais, Region, Provincia, Comuna, Ciudad

def lista_paises(request):
    paises = Pais.objects.all()
    return render(request, 'ubicaciones/lista_paises.html', {'paises': paises})

def detalle_pais(request, pais_id):
    pais = get_object_or_404(Pais, id=pais_id)
    return render(request, 'ubicaciones/detalle_pais.html', {'pais': pais})

def lista_regiones(request, pais_id):
    pais = get_object_or_404(Pais, id=pais_id)
    regiones = Region.objects.filter(pais=pais)
    return render(request, 'ubicaciones/lista_regiones.html', {'pais': pais, 'regiones': regiones})

def detalle_region(request, region_id):
    region = get_object_or_404(Region, id=region_id)
    return render(request, 'ubicaciones/detalle_region.html', {'region': region})

def lista_provincias(request, region_id):
    region = get_object_or_404(Region, id=region_id)
    provincias = Provincia.objects.filter(region=region)
    return render(request, 'ubicaciones/lista_provincias.html', {'region': region, 'provincias': provincias})

def detalle_provincia(request, provincia_id):
    provincia = get_object_or_404(Provincia, id=provincia_id)
    return render(request, 'ubicaciones/detalle_provincia.html', {'provincia': provincia})

def lista_comunas(request, provincia_id):
    provincia = get_object_or_404(Provincia, id=provincia_id)
    comunas = Comuna.objects.filter(provincia=provincia)
    return render(request, 'ubicaciones/lista_comunas.html', {'provincia': provincia, 'comunas': comunas})

def lista_ciudades(request, provincia_id):
    provincia = get_object_or_404(Provincia, id=provincia_id)
    ciudades = Ciudad.objects.filter(provincia=provincia)
    return render(request, 'ubicaciones/lista_ciudades.html', {'provincia': provincia, 'ciudades': ciudades})

def detalle_comuna(request, comuna_id):
    comuna = get_object_or_404(Comuna, id=comuna_id)
    return render(request, 'ubicaciones/detalle_comuna.html', {'comuna': comuna})

def detalle_ciudad(request, ciudad_id):
    ciudad = get_object_or_404(Ciudad, id=ciudad_id)
    return render(request, 'ubicaciones/detalle_ciudad.html', {'ciudad': ciudad})
