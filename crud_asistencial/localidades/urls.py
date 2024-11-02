from django.urls import path
from . import views

urlpatterns = [
    path("ingresar-localidades/", views.ingresar_localidades, name="ingresar_localidades"),
    path("verificar-duplicado/", views.verificar_duplicado_ajax, name="verificar_duplicado_ajax"),
    path("obtener-regiones/", views.obtener_regiones, name="obtener_regiones"),
    path("obtener-provincias/", views.obtener_provincias, name="obtener_provincias"),
    path("", views.inicio, name="inicio"),  # Suponiendo que tienes una vista de inicio
]
