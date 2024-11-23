from django.db import models
from registro.models import Patient
from data.utils import calcular_edad

# Create your models here.
class MedicalRecord(models.Model):
    patient = models.OneToOneField(Patient,on_delete=models.CASCADE, related_name="medical_record")
    age_at_visit = models.PositiveIntegerField(blank=True, null=True, help_text="Edad del paciente al momento de la atención")
    allergies = models.TextField(blank=True, null=True, help_text="Listado de alergias")
    treatments = models.TextField(blank=True, null=True, help_text="Historial de tratamientos")
    exams = models.TextField(blank=True, null=True, help_text="Resultado de exámenes médicos")
    vital_signs = models.JSONField(blank=True, null=True, help_text = "Signos vitales registrados")
    blood_type = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """Sobrescribe el método save para calcular la edad del paciente automáticamente."""
        if self.patient.date_of_birth:
            self.age_at_visit = calcular_edad(self.patient.date_of_birth)
        super().save(*args, **kwargs)

    def __str__(self) :
        return f"Ficha Médica de {self.patient.name} - Edad: {self.age_at_visit} años"
    
    class Meta:
        verbose_name = "Ficha Médica"
        verbose_name_plural = "Fichas Médicas"