from rest_framework import serializers
from .models import Pais #, Region, Provincia, Comuna, Ciudad
from utils import remover_acentos, verificar_duplicado, validate_codigo_telefonico, formatear_texto, validate_nombre

class PaisSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['id', 'nombre_pais','codigo_telefonico_pais']

    def validate_nombre_pais(self, value):
        # Eliminar acentos y caracteres especiales
        value = remover_acentos(value)

        # Luego formatear el texto
        value = formatear_texto(value)

        # Validar el nombre para que no contenga caracteres inválidos
        validate_nombre(value)

        # Verificar que el nombre no esté duplicado
        verificar_duplicado('localidades.Pais', 'nombre_pais', value)

        try:
            Pais.objects.get(nombre_pais=value)
            raise serializers.ValidationError("El país ya existe.")
        except Pais.DoesNotExist:
            return value
    
    def validate_codigo_telefonico_pais(self, value):
        # Validar y formatear el código telefónico antes de verificar duplicados
        value = validate_codigo_telefonico(value)
        return value

"""
class RegionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'nombre_region', 'codigo_telefonico_region', 'pais']

    def validate_nombre_region(self, value):
        # Eliminar acentos y caracteres especiales
        value = remover_acentos(value)

        # Luego formatear el texto
        value = formatear_texto(value)

        # Validar el nombre para que no contenga caracteres inválidos
        validate_nombre(value)

        # Verificar que el nombre no esté duplicado
        verificar_duplicado('localidades.Region', 'nombre_region', value)

        return value
    
    def validate_codigo_telefonico_region(self, value):
        # Validar y formatear el código telefónico antes de verificar duplicados
        value = validate_codigo_telefonico(value)
        return value
        
class ProvinciaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ['id', 'nombre_provincia', 'region']

    def validate_nombre_provincia(self, value):
        # Eliminar acentos y caracteres especiales
        value = remover_acentos(value)

        # Luego formatear el texto
        value = formatear_texto(value)

        # Validar el nombre para que no contenga caracteres inválidos
        validate_nombre(value)

        # Verificar que el nombre no esté duplicado
        verificar_duplicado('localidades.Provincia', 'nombre_provincia', value)

        return value

class ComunaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ['id', 'nombre_comuna', 'provincia']

    def validate_nombre_comuna(self, value):
        # Eliminar acentos y caracteres especiales
        value = remover_acentos(value)

        # Luego formatear el texto
        value = formatear_texto(value)

        # Validar el nombre para que no contenga caracteres inválidos
        validate_nombre(value)

        # Verificar que el nombre no esté duplicado
        verificar_duplicado('localidades.Comuna', 'nombre_comuna', value)

        return value

class CiudadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ['id', 'nombre_ciudad', 'provincia']

    def validate_nombre_ciudad(self, value):
        # Eliminar acentos y caracteres especiales
        value = remover_acentos(value)

        # Luego formatear el texto
        value = formatear_texto(value)

        # Validar el nombre para que no contenga caracteres inválidos
        validate_nombre(value)

        # Verificar que el nombre no esté duplicado
        verificar_duplicado('localidades.Ciudad', 'nombre_ciudad', value)

        return value"""