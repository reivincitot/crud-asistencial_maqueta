from rest_framework import serializers
from .models import Regions, Province, Commune, Address

class RegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields = "__all__"

class ProvinceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = "__all__"

class CommuneSerializers(serializers.ModelSerializer):
    class Meta:
        model = Commune 
        fields = "__all__"

class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"