from django.urls import path
from . import views

urlpatterns = [
    path("paises/", views.lista_paises, name="lista_paises"),
    path("pais/<int:pais_id>/", views.detalle_pais, name="detalle_pais"),
    path("pais/<int:pais_id/regiones/", views.lista_regiones, name="lista_regiones"),
    path("region/<int:region_id>/", views.detalle_region, name="detalle_region"),
    path(
        "region/<int:region_id/provincias>/",
        views.lista_provincias,
        name="lista_provincias",
    ),
    path(
        "provincia/<int:provincia_id>/",
        views.detalle_provincia,
        name="detalle_provincia",
    ),
    path(
        "provincia/<int:provincia_id>/comunas/",
        views.lista_comunas,
        name="lista_comunas",
    ),
    path(
        "provincia/<int:provincia_id>/ciudades/",
        views.lista_ciudades,
        name="lista_ciudades",
    ),
    path("comuna/<int:comuna_id>/", views.detalle_comuna, name="detalle_comuna"),
    path("ciudad/<int:ciudad_id>/", views.detalle_ciudad, name="detalle_ciudad"),
]
