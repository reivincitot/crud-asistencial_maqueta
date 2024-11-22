from rest_framework import serializers
from .models import Patient, ProfesionalDeSalud


class PatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

class ProfesionaDeSaluidSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfesionalDeSalud
        fields = "__all__"