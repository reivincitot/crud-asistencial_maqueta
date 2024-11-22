from django.db import models
from data.utils import calcular_edad
from locations.models import Address


class AbstractPerson(models.Model):
    name=models.CharField(max_length=100, blank=False, null=False, default="Persona")
    rut = models.CharField(max_length=12, unique=True, blank=False, null=False, db_index=True)
    date_of_birth = models.DateField()
    email = models.EmailField()
    cell_phone_number = models.CharField(max_length=12, blank=True, null=False, default="+56900000000")

    def get_age(self):
        """
        Calcula la edad a partir de la fecha de nacimiento.
        """
        return calcular_edad(self.date_of_birth)
    
    def __str__(self):
        return f"Nombre:{self.name}, Rut: {self.rut},"

    class Meta:
        abstract = True


class ProfesionalDeSalud(AbstractPerson):
    specialty = models.CharField(max_length=100)
    place_of_origin = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True, help_text="Lugar de procedencia, si es diferente a la dirección actual")
    medic_rol_number = models.CharField(max_length=20, unique=True, blank=False)

    def __str__(self):
        return f"Nombre:{self.name}, Especialidad: {self.specialty}"
    
    class Meta:
        verbose_name = "Profesional de la salud"
        verbose_name_plural = "Profesionales de la salud"

class Patient(AbstractPerson):
    medical_record_number = models.CharField(max_length=20, unique=True, blank=False, null=False)
    

    def __str__(self):
        return f"{self.name} Nº de Ficha :{self.medical_record_number}"
    
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
