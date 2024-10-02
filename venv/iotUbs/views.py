from django.http import JsonResponse

def equipamentos(request):
    if request.method == 'GET':
        equipamento = {
            'id_equipamento':12345, 
            'nome_equipamento':'Geladeira',
            }
        return JsonResponse(equipamento)
    
##
