from django.db import models
from registro.models import AbastractPerson
from data.utils import calcular_edad

# Helper para incrementar sufijos
def increment_suffix(suffix):
    """
    Incrementa un sufijo alfabético (A, B, C, ..., Z, AA, AB, ..., AZ, BA, ...)
    """
    if suffix == 'Z':
        return 'AA'
    elif suffix == 'ZZ':
        return 'AAA'
    else:
        return ''.join(
            chr(((ord(char) - 65 + 1) % 26) + 65) if i == len(suffix) - 1 else char
            for i, char in enumerate(suffix[::-1])
        )[::-1]

class MedicalRecord(models.Model):
    patient = models.OneToOneField(AbastractPerson, on_delete=models.CASCADE, related_name="medical_record")
    medical_record_number = models.CharField(unique=True, blank=False, null=False, db_index=True)
    age_at_visit = models.PositiveIntegerField(blank=True, null=True, help_text="Edad del paciente al momento de la atención")
    allergies = models.TextField(blank=True, null=True, help_text="Listado de alergias")
    treatments = models.TextField(blank=True, null=True, help_text="Historial de tratamientos")
    exams = models.TextField(blank=True, null=True, help_text="Resultado de exámenes médicos")
    vital_signs = models.JSONField(blank=True, null=True, help_text="Signos vitales registrados")
    blood_type = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def generate_medical_record_number(name, father_lastname, mother_lastname, rut):
        """
        Genera un número de ficha médica único basado en el nombre, apellidos y rut del paciente,
        con un sufijo que se incrementa si se detecta una colisión.
        """
        # Helper para numerizar letras
        def numerize_letter(letter):
            return ord(letter.upper()) - 64  # Convierte 'A' a 1, 'B' a 2, ...'Z' a 26

        # Generar bloques de numerización agrupada
        def numerize_name_blocks(name_part):
            blocks = []
            for i in range(0, min(2, len(name_part)), 2):
                pair = name_part[i:i + 2]  # Toma de 1 a 2 caracteres
                block = ''.join(str(numerize_letter(char)) for char in pair if char.isalpha())
                blocks.append(block)
            return ''.join(blocks)

        # Procesar los nombres y apellidos
        name_block = numerize_name_blocks(name)
        second_name_block = ""
        if len(name.split()) > 1:
            second_name_block = numerize_name_blocks(name.split()[1])
        father_lastname_block = numerize_name_blocks(father_lastname)
        mother_lastname_block = numerize_name_blocks(mother_lastname)

        # Procesar el Rut (sin el dígito verificador)
        rut_digits = [int(digit) for digit in rut[:-2][::-1]]  # Invierte y convierte a enteros
        factors = [2, 3, 4, 5, 6, 7]
        rut_sum = sum(rut_digits[i % len(factors)] * factors[i % len(factors)] for i in range(len(rut_digits)))

        # Formato base del número de ficha
        base_medical_record_number = f"{name_block}-{second_name_block}-{father_lastname_block}-{mother_lastname_block}-{rut_sum}"

        # Verificar colisiones y agregar sufijo
        suffix = 'A'
        while MedicalRecord.objects.filter(medical_record_number=f"{base_medical_record_number}/{suffix}").exists():
            # Si ya existe el número con ese sufijo, incrementar el sufijo
            suffix = increment_suffix(suffix)

        # Retornar el número de ficha con el sufijo correspondiente
        return f"{base_medical_record_number}/{suffix}"

    def save(self, *args, **kwargs):
        """
        Sobrescribe el método save para calcular la edad del paciente automáticamente y generar el número de ficha médica si no existe.
        """
        if not self.medical_record_number:
            self.medical_record_number = self.generate_medical_record_number(
                self.patient.name, 
                self.patient.father_lastname, 
                self.patient.mother_lastname, 
                self.patient.rut
            )
        if self.patient.date_of_birth:
            self.age_at_visit = calcular_edad(self.patient.date_of_birth)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Ficha Médica de {self.patient.name} - Edad: {self.age_at_visit} años"

    class Meta:
        verbose_name = "Ficha Médica"
        verbose_name_plural = "Fichas Médicas"
