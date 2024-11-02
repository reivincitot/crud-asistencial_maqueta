from datetime import date
from django.core.exceptions import ValidationError
import re
import unidecode
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
    texto_sin_acentos = unidecode(texto)
    
    # Capitalizar cada palabra excepto la conjunción "y"
    texto_formateado = ' '.join(
        [word.capitalize() if word.lower() != 'y' else 'y' for word in texto_sin_acentos.split()]
    )
    
    return texto_formateado

def verificar_duplicado(modelo_str, campo, valor):
    """
    Verifica si existe un registro en un modelo específico con un valor duplicado para un campo específico.
    
    Parameters:
    - modelo_str (str): El nombre del modelo en formato 'app_label.ModelName'.
    - campo (str): El nombre del campo en el que se verificará la duplicación.
    - valor: El valor que se busca duplicado.

    Raises:
    - ValidationError: Si el valor ya existe en el modelo para el campo especificado.
    """
    # Obtener el modelo a partir del nombre en formato 'app_label.ModelName'
    try:
        modelo = apps.get_model(modelo_str)
    except LookupError:
        raise ValidationError(f"El modelo '{modelo_str}' no existe.")

    # Verificar si existe el valor duplicado (ignorar mayúsculas/minúsculas)
    if modelo.objects.filter(**{f"{campo}__iexact": valor}).exists():
        raise ValidationError(f"El valor '{valor}' ya existe para el campo '{campo}' en {modelo_str}.")

def validate_nombre(value):
    """
    Valida que un nombre no contenga caracteres inválidos y que no tenga espacios al inicio o al final.
    """
    value = value.strip()
    if not re.match(r'^[a-zA-Z\s]+$', value):
        raise ValidationError("El nombre solo puede contener letras y espacios.")
    return value

def verificar_duplicado_dinamico(nombre_modelo, campo, valor):
    """
    Valida la existencia de un campo y verifica que no haya duplicados en el modelo especificado por su nombre.
    """
    modelo = apps.get_model('direcciones', nombre_modelo)
    return modelo.objects.filter(**{campo: valor}).exists()
