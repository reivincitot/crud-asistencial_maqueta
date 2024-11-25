from django.db import models
from registro.models import AbstractPerson

class Patient(AbstractPerson):
    medical_record_number = models.CharField(unique=True, blank=True, null=True, db_index=True)

    def __str__(self):
        return f"{self.name} Nº de Ficha :{self.medical_record_number}"

    def increment_suffix(self, suffix):
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

    def generate_medical_record_number(self):
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
        name_block = numerize_name_blocks(self.name)
        second_name_block = ""
        if len(self.name.split()) > 1:
            second_name_block = numerize_name_blocks(self.name.split()[1])
        father_lastname_block = numerize_name_blocks(self.father_lastname)
        mother_lastname_block = numerize_name_blocks(self.mother_lastname)

        # Procesar el Rut (sin el dígito verificador)
        rut_digits = [int(digit) for digit in self.rut[:-2][::-1]]  # Invierte y convierte a enteros
        factors = [2, 3, 4, 5, 6, 7]
        rut_sum = sum(rut_digits[i % len(factors)] * factors[i % len(factors)] for i in range(len(rut_digits)))

        # Formato base del número de ficha
        base_medical_record_number = f"{name_block}-{second_name_block}-{father_lastname_block}-{mother_lastname_block}-{rut_sum}"

        # Verificar colisiones y agregar sufijo
        suffix = 'A'
        while Patient.objects.filter(medical_record_number=f"{base_medical_record_number}/{suffix}").exists():
            # Si ya existe el número con ese sufijo, incrementar el sufijo
            suffix = self.increment_suffix(suffix)

        # Asignar el número de ficha médica generado
        return f"{base_medical_record_number}/{suffix}"

    def save(self, *args, **kwargs):
        """
        Sobrescribe el método save para generar automáticamente el número de ficha médica
        si no existe.
        """
        if not self.medical_record_number:
            self.medical_record_number = self.generate_medical_record_number()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
