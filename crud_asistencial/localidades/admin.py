from django.contrib import admin
from .models import Pais, Region, Provincia, Comuna, Ciudad
# Register your models here.

admin.site.register(Pais)
admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)
admin.site.register(Ciudad)