from rest_framework import serializers
from .models import Patient, ProfesionalDeSalud, Employee
from data.utils import verificar_duplicado, validate_nombre, formatear_texto, validar_rut

class PatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
    
    def validate_name(self, value):
        """Valida y formatea el nombre antes de guardarlo."""
        # Solo formatear el nombre, no verificar duplicados
        validate_nombre(value)
        return formatear_texto(value)

    def validate_rut(self, value):
        """Valida el formato del RUT y verifica duplicados."""
        value = validar_rut(value)
        instance_id = self.instance.id if self.instance else None
        verificar_duplicado('registro.Patient', 'rut', value, instance_id)
        return value

class ProfesionalDeSaludSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfesionalDeSalud
        fields = "__all__"

    def validate_rut(self, value):
        """Valida el formato del RUT y verifica duplicados."""
        value = validar_rut(value)
        instance_id = self.instance.id if self.instance else None
        verificar_duplicado('registro.ProfesionalDeSalud', 'rut', value, instance_id)
        return value

    def validate_medic_rol_number(self, value):
        """Valida el formato del número del rol médico"""
        verificar_duplicado('registro.ProfesionalDeSalud','medic_rol_number', value)
        return value    
    
    def validate_name(self, value):
        """Valida y formatea el nombre antes de guardarlo."""
        validate_nombre(value)
        return formatear_texto(value)
    
class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    def validate_name(self, value):
        """Valida y formatea el nombre antes de guardarlo."""
        # Solo formatear el nombre, no verificar duplicados
        validate_nombre(value)
        return formatear_texto(value)

    def validate_rut(self, value):
        """Valida el formato del RUT y verifica duplicados."""
        value = validar_rut(value)
        instance_id= self.instance.id if self.instance else None
        verificar_duplicado('registro.Employee', 'rut', value, instance_id)
        return value
