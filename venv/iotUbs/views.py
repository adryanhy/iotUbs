from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Equipamentos, EquipmentLog
from .serializers import EquipmentSerializer
from .serializers import EquipmentLogSerializer
from rest_framework import generics


@api_view(['GET', 'POST'])
def equipamentos_lista(request):
    if request.method == 'GET':
        equipamentos = Equipamentos.objects.all()
        serializer = EquipmentSerializer(equipamentos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            equipamentos = serializer.instance
            log_new_equipment(equipamentos)
            if equipamentos.temperature < 2 or equipamentos.temperature > 8:
                print(f"Alerta: A temperatura do equipamento '{equipamentos.name}' está fora do limite seguro!")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
    
def equipment_log_list(request):
    logs = EquipmentLog.objects.all().order_by('-created_at')  # Ordenando do mais recente ao mais antigo
    serializer = EquipmentLogSerializer(logs, many=True)
    return Response(serializer.data)

    
@api_view(['GET', 'PUT', 'DELETE'])
def detalhes_equipamentos(request, pk):
    try:
        equipamento = Equipamentos.objects.get(pk=pk)
    except Equipamentos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EquipmentSerializer(equipamento)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = EquipmentSerializer(equipamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        equipamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##logs
def log_new_equipment(equipamento):
    EquipmentLog.objects.create(
        equipment_name=equipamento.name,
        temperature=equipamento.temperature,
        latitude=equipamento.latitude,
        longitude=equipamento.longitude,
        status=equipamento.status
    )