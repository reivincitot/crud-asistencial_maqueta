from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient, ProfesionalDeSalud, Employee
from .serializers import PatientSerializers, ProfesionalDeSaludSerializers, EmployeeSerializers


def home_view(request):
    """
    Renderiza la página de inicio.
    """
    return render(request, "home.html")

# ViewSets par los serializers
class PatientViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar pacientes.
    """

    queryset = Patient.objects.all()
    serializer_class = PatientSerializers

class ProfesionalDeSaludViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar a los profesionales de la salud.
    """

    queryset = ProfesionalDeSalud.objects.all()
    serializer_class = ProfesionalDeSaludSerializers

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar a los empleados.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

def registro_view(request):
    """
    Renderiza el formulario de registro de persona.
    """
    return render(request, "registro/registro.html")