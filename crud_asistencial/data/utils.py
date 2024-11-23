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

def verificar_duplicado(modelo_str, campo, valor, instance_id=None):
    """
    Verifica si existe un registro duplicado en un modelo específico, ignorando un registro específico si es necesario.
    """
    try:
        modelo = apps.get_model(modelo_str)
    except LookupError:
        raise ValidationError(f"El modelo '{modelo_str}' no existe.")
    
    valor_normalizado = formatear_texto(valor)

    # Filtrar registros duplicados, excluyendo la instancia en edición
    query = modelo.objects.filter(**{f"{campo}__iexact": valor_normalizado})
    if instance_id:
        query = query.exclude(pk=instance_id)

    if query.exists():
        raise ValidationError(f"El valor '{valor_normalizado}' ya existe para el campo '{campo}' en {modelo_str}.")


def validate_nombre(value):
    """
    Valida que un nombre no contenga caracteres inválidos y que no tenga espacios al inicio o al final.
    """
    value = value.strip()
    if not re.match(r'^[a-zA-Z\s]+$', value):
        raise ValidationError("El nombre solo puede contener letras y espacios.")
    return value

def validar_rut(rut):
    """
    Valida un RUT chileno, incluyendo su dígito verificador.
    Esta función es genérica y se puede usar para pacientes, profesionales de la salud u otros.
    
    Parameters:
    - rut (str): El RUT a validar en formato '12345678K' o '12.345.678-K'.

    Returns:
    - str: El RUT limpio (sin puntos ni guiones) si es válido.

    Raises:
    - ValidationError: Si el RUT no tiene un formato válido o el dígito verificador no es correcto.
    """
    # Limpiar el RUT de puntos y guiones
    rut = rut.upper().replace(".", "").replace("-", "")
    
    # Verificar el formato básico
    if not re.match(r"^\d{1,8}[0-9K]$", rut):
        raise ValidationError("El RUT debe tener un formato válido (Ej: 12345678K).")
    
    # Separar el cuerpo del RUT y el dígito verificador
    cuerpo = rut[:-1]
    dv = rut[-1]

    # Cálculo del dígito verificador
    suma = 0
    multiplicador = 2
    for c in reversed(cuerpo):
        suma += int(c) * multiplicador
        multiplicador = 9 if multiplicador == 7 else multiplicador + 1
    
    resultado = 11 - (suma % 11)
    dv_calculado = "K" if resultado == 10 else "0" if resultado == 11 else str(resultado)

    # Validar el dígito verificador
    if dv_calculado != dv:
        raise ValidationError("El dígito verificador del RUT es incorrecto.")
    
    return rut  # Retornar el RUT limpio
