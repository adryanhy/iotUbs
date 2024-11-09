from rest_framework import serializers
from .models import Equipamentos, EquipmentLog

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipamentos
        fields = ['id', 'name', 'temperature', 'latitude', 'longitude', 'status'] 


class EquipmentLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentLog
        fields = ['id', 'name', 'temperature', 'latitude', 'longitude', 'status', 'created_at']

    # def validate_temperature(self, value):
    #         if value < 2 or value > 8:
    #             raise serializers.ValidationError("Temperatura fora dos limites seguros para armazenamento.")
    #         return value


# class TransporteHistoricoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TransporteHistorico
#         fields = ['data', 'temperatura', 'latitude', 'longitude']