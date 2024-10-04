from rest_framework import serializers
from .models import Equipamentos

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipamentos
        fields = ['id', 'name', 'temperature', 'location', 'status']  # Campos que serão serializados
