# views.py
from django.shortcuts import render, redirect
from .forms import LocalidadesForm
from .models import Pais, Region, Provincia, Comuna, Ciudad
from utils import formatear_texto
from django.http import JsonResponse

def ingresar_localidades(request):
    if request.method == "POST":
        form = LocalidadesForm(request.POST)
        if form.is_valid():
            # Guardar nuevos datos solo si se proporcionaron
            if form.cleaned_data["nuevoPais"]:
                Pais.objects.create(
                    nombre=form.cleaned_data["nuevoPais"],
                    codigo=form.cleaned_data["nuevoCodigoPais"],
                )
            if form.cleaned_data["nuevaRegion"]:
                Region.objects.create(
                    nombre=form.cleaned_data["nuevaRegion"],
                    codigo=form.cleaned_data["nuevoCodigoRegion"],
                )
            if form.cleaned_data["nuevaProvincia"]:
                Provincia.objects.create(nombre=form.cleaned_data["nuevaProvincia"])
            if form.cleaned_data["nuevaComuna"]:
                Comuna.objects.create(nombre=form.cleaned_data["nuevaComuna"])
            if form.cleaned_data["nuevaCiudad"]:
                Ciudad.objects.create(nombre=form.cleaned_data["nuevaCiudad"])
            return redirect("inicio")
    else:
        form = LocalidadesForm()

    paises = Pais.objects.all()
    regiones = Region.objects.all()
    provincias = Provincia.objects.all()
    comunas = Comuna.objects.all()
    ciudades = Ciudad.objects.all()

    context = {
        "form": form,
        "paises": paises,
        "regiones": regiones,
        "provincias": provincias,
        "comunas": comunas,
        "ciudades": ciudades,
    }
    return render(request, "localidades/localidades.html", context)

def verificar_duplicado_ajax(request):
    nombre = request.GET.get("nombre", "")
    nombre_formateado = formatear_texto(nombre)
    existe = Region.objects.filter(nombre__iexact=nombre_formateado).exists()
    return JsonResponse({"existe": existe})

# Vista para obtener regiones de un país específico
def obtener_regiones(request):
    pais_id = request.GET.get("pais_id")
    regiones = Region.objects.filter(pais_id=pais_id).values("id", "nombre")
    return JsonResponse(list(regiones), safe=False)

# Vista para obtener provincias de una región específica
def obtener_provincias(request):
    region_id = request.GET.get("region_id")
    provincias = Provincia.objects.filter(region_id=region_id).values("id", "nombre")
    return JsonResponse(list(provincias), safe=False)

# Vista de inicio
def inicio(request):
    return render(request, "home.html")
