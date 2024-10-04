from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Equipamentos
from .serializers import EquipmentSerializer

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT'])
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
    
    ##elif request.method == 'DELETE':
    ##equipamento.delete()
    ##return Response(status=status.HTTP_204_NO_CONTENT)