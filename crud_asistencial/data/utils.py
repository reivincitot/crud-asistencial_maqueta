from datetime import date
from django.core.exceptions import ValidationError
import re
from unidecode import unidecode
from django.apps import apps


def calcular_edad(fecha_de_nacimiento):
    """
    Calcula la edad a partir de la fecha de nacimiento.
    """
    today = date.today()
    age = today.year - fecha_de_nacimiento.year
    if (today.month, today.day) < (fecha_de_nacimiento.month, fecha_de_nacimiento.day):
        age -= 1
    return age

def remover_acentos(texto):
    """
    Remueve acentos y caracteres especiales de un texto.
    """
    return unidecode(texto)

def formatear_texto(texto):
    """
    Formatea un texto para que cada palabra comience con mayúscula, excepto 'y'.
    Elimina acentos y caracteres especiales antes de formatear.
    
    Parameters:
    - texto (str): El texto a formatear.

    Returns:
    - str: Texto formateado, listo para guardar en la base de datos.
    """
    # Remover acentos y convertir el texto a título
    texto_sin_acentos = remover_acentos(texto)
    texto_formateado = texto_sin_acentos.strip().lower()

    return texto_formateado

def verificar_duplicado(modelo_str, campo, valor):
    """
    Verifica si existe un registro en un modelo específico con un valor duplicado para un campo específico.
    """
    try:
        modelo = apps.get_model(modelo_str)
    except LookupError:
        raise ValidationError(f"El modelo '{modelo_str}' no existe.")
    
    valor_normalizado = formatear_texto(valor)

    # Verificar si existe el valor duplicado (ignorar mayúsculas/minúsculas)
    if modelo.objects.filter(**{f"{campo}__iexact": valor_normalizado}).exists():
        raise ValidationError(f"El valor '{valor_normalizado}' ya existe para el campo '{campo}' en {modelo_str}.")

def validate_nombre(value):
    """
    Valida que un nombre no contenga caracteres inválidos y que no tenga espacios al inicio o al final.
    """
    value = value.strip()
    if not re.match(r'^[a-zA-Z\s]+$', value):
        raise ValidationError("El nombre solo puede contener letras y espacios.")
    return value

def validate_codigo_telefonico(value):
    # Validar el código telefónico para País
    if not re.match(r'^\+\d{1,4}$', value) and not re.match(r'^\d{2}$', value):
        raise ValidationError(f"El código telefónico '{value}' no tiene un formato válido")

    # Obtener los modelos 'Pais' y 'Region' de la app 'localidades'
    Pais = apps.get_model('localidades', 'Pais')
    Region = apps.get_model('localidades', 'Region')
    
    # Verificar si el código telefónico ya existe en la tabla de Pais
    if Pais.objects.filter(codigo_telefonico_pais=value).exists():
        raise ValidationError(f"El código telefónico '{value}' ya está registrado para un país.")
    
    # Verificar si el código telefónico ya existe en la tabla de Region
    if Region.objects.filter(codigo_telefonico_region=value).exists():
        raise ValidationError(f"El código telefónico '{value}' ya está registrado para una región.")

    return value