from django.db import models


# Create your models here.
class Pais(models.Model):
    """
    Modelo que representa un país.

    Atributos:
        nombre_pais (CharField): Nombre del país, debe ser único y se guardará en minúsculas.
        codigo_pais (CharField): Código telefónico del país, único.

    Métodos:
        __str__(): Devuelve una representación legible del objeto.
    """

    nombre_pais = models.CharField(max_length=100, unique=True, db_index=True)
    codigo_pais = models.CharField(max_length=3, unique=True)

    def save(self, *args, **kwargs):
        self.nombre_pais = self.nombre_pais.lower()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Pais:{self.nombre_pais}, Código País: {self.codigo_pais}"

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"


class Region(models.Model):
    """
    Modelo que representa una región dentro de un país.

    Atributos:
        nombre_region (CharField): Nombre de la región, debe ser único.
        pais (ForeignKey): Relación con el modelo Pais.
        codigo_telefonico_region (CharField): Código telefónico de la región, puede ser nulo y debe ser único.

    Métodos:
        __str__(): Devuelve una representación legible del objeto.
    """

    nombre_region = models.CharField(
        max_length=100, unique=True, blank=False, db_index=True
    )
    codigo_region = models.CharField(max_length=3, blank=True, null=True, unique=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.nombre_region = self.nombre_region.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Nombre de la Región: {self.nombre_region}, Código telefónico de la Región: {self.codigo_region}"

    class Meta:
        verbose_name = "Región"
        verbose_name_plural = "Regiones"


class Provincia(models.Model):
    """
    Modelo que representa una provincia dentro de una región.

    Atributos:
        nombre_provincia (CharField): Nombre de la provincia, puede ser nulo y debe ser único.
        region (ForeignKey): Relación con el modelo Region.

    Métodos:
        __str__(): Devuelve una representación legible del objeto.
    """

    nombre_provincia = models.CharField(
        max_length=100, unique=True, blank=True, null=True, db_index=True
    )
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, db_index=True
    )

    def save(self, *args, **kwargs):
        self.nombre_provincia = self.nombre_provincia.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.region}, Provincia:{self.nombre_provincia}"
    
    class Meta:
        unique_together = ('nombre_provincia', 'region')
        verbose_name ="Provincia"
        verbose_name_plural ="Provincias"

class Comuna(models.Model):
    """
    Modelo que representa una comuna dentro de una provincia.

    Atributos:
        nombre_comuna (CharField): Nombre de la comuna, debe ser único.
        provincia (ForeignKey): Relación con el modelo Provincia.

    Métodos:
        __str__(): Devuelve una representación legible del objeto.
    """
    nombre_comuna = models.CharField(max_length=100, unique=True,)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.nombre_comuna = self.nombre_comuna.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre_comuna}, de la provincia de: {self.provincia}"
    
    class Meta:
        verbose_name = "Comuna"
        verbose_name_plural = "Comunas"

class Ciudad(models.Model):
    """
    Modelo que representa una ciudad dentro de una provincia.

    Atributos:
        nombre_ciudad (CharField): Nombre de la ciudad, debe ser único.
        provincia (ForeignKey): Relación con el modelo Provincia.

    Métodos:
        __str__(): Devuelve una representación legible del objeto.
    """
    nombre_ciudad = models.CharField(max_length=100, unique=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)