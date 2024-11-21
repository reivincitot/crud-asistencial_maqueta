from django.db import models
from data.utils import calcular_edad
# Create your models here.

class Persona(models.Model):
    name=models.CharField(max_length=100, blank=False, null=False, default="Persona")
    rut = models.CharField(max_length=12, unique=True, blank=False, null=False, db_index=True)
    date_of_birth = models.DateField()
    email = models.EmailField()
    cell_phone_number = models.CharField(max_length=12, blank=True, null=False, default="+56900000000")
    
    # Dirección
    region = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    numeration = models.IntegerField()

    class Meta:
        abstract = True

class ProfesionalDeSalud(Persona):
    specialty = models.CharField(max_length=100)
    place_of_origin = models.CharField(max_length=100)
    medic_rol_number = models.CharField(max_length=20, unique=True, blank=False)

