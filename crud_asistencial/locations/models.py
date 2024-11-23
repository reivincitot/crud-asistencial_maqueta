from django.db import models

# Create your models here.
class Regions(models.Model):
    name = models.CharField(max_length=30)
    regional_phone_code = models.CharField(max_length=4)
    
    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiones"

class Province(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"

class Commune(models.Model):
    name = models.CharField(max_length=50)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Comuna"
        verbose_name_plural= "Comunas"

class Address(models.Model):
    street = models.CharField(max_length=200)
    number = models.CharField(max_length=8)
    apartment = models.CharField(max_length=6)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)

    def __str__(self):
            return f"{self.street}, {self.number}, {self.commune.name}"
    
    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"