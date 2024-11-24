from django.db import models

# Create your models here.
class ProfesionalDeSalud(AbstractPerson):
    specialty = models.CharField(max_length=100, db_index=True)
    medic_rol_number = models.CharField(max_length=20, unique=True, blank=False, db_index=True)

    def __str__(self):
        return f"Nombre:{self.name}, Especialidad: {self.specialty}"

    class Meta:
        verbose_name = "Profesional de la salud"
        verbose_name_plural = "Profesionales de la salud"