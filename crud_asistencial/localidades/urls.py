from django.urls import path
from .views import home, LocalidadesTemplateView, PaisListView #, RegionListView, ProvinciaListView, ComunaCreateView, CiudadCreateView 

urlpatterns = [
    path('', home, name='home'),
    path('ingresar-localidades/', LocalidadesTemplateView.as_view(), name='ingresar_localidades'),
    path('localidades/', PaisListView.as_view(), name='pais-list'),
    # path('regiones/', RegionListView.as_view(), name='region-list'),
    # path('provincias/', ProvinciaListView.as_view(), name='provincia-list'),
    # path('comunas/', ComunaCreateView.as_view(), name='comuna-create'),
    # path('ciudades/', CiudadCreateView.as_view(), name='ciudad-create'),
    
]