from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import home_view, PatientViewSet, ProfesionalDeSaludViewSet, EmployeeViewSet, registro_view

# Router para los ViewSets
router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'profesionales', ProfesionalDeSaludViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', home_view, name='home'),
    path('api/', include(router.urls)), # Rutas para la API
    path('registro/', registro_view, name='registro')
]
