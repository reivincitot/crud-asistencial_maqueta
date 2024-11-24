from django.db import models
from registro.models import AbstractPerson
from medical_record.models import MedicalRecord


class Patient(AbstractPerson):
    medical_record_number = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} Nº de Ficha :{self.medical_record_number}"

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"