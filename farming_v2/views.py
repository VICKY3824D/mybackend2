from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from farming_v2.models import Petani
from farming_v2.serializers import PetaniSerializer

@csrf_exempt

def petani_list(request):
    
    """
    List all petani, or create a new petani.
    """
    
    if request.method == 'GET':
        petani = Petani.objects.all()
        serializer = PetaniSerializer(petani, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PetaniSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)