from django.urls import path, include
from .views import LocalidadesTemplateView, PaisListView, home
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'api/paises', PaisListView, basename='pais')


urlpatterns = [
    path('home/', home, name='home'),
    path('localidades/', LocalidadesTemplateView.as_view(), name='ingresar_localidades'),  # Aquí cambia el nombre de 'localidades' a 'ingresar_localidades'
    path('', include(router.urls)),
]
