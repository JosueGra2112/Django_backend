from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from .models import RadioStation
from .serializers import RadioStationSerializer

class RadioStationList(APIView):

    #Listar estaciones de radio 
    
    def get(self, request):
        stations = RadioStation.objects.all()
        serializer = RadioStationSerializer(stations, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):

        # Estaction de radio nueva
        serializer = RadioStationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def update_favorite_status(request):
  
        #Agregar a favoritos
    try:
        data = request.data 
        station_id = data.get('id')
        is_favorite = data.get('is_favorite')
        
        station = get_object_or_404(RadioStation, id=station_id)# Verifica si existe la estación
       
        station.is_favorite = is_favorite  #Actualiza el estado de favorito
        station.save() 

        return JsonResponse({"message": "Favorite status updated successfully"})
    except RadioStation.DoesNotExist:
        return JsonResponse({"error": "Station not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
