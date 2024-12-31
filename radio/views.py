from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from .models import RadioStation
from .serializers import RadioStationSerializer

class RadioStationList(APIView):
    """
    Endpoint para listar todas las estaciones de radio y crear una nueva estación.
    """
    def get(self, request):
        stations = RadioStation.objects.all()
        serializer = RadioStationSerializer(stations, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        """
        Crear una nueva estación de radio.
        """
        serializer = RadioStationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def update_favorite_status(request):
    """
    Endpoint para actualizar el estado de favorito de una estación de radio.
    """
    try:
        data = request.data  # Obtiene los datos enviados desde el cliente
        station_id = data.get('id')
        is_favorite = data.get('is_favorite')

        # Verifica si existe la estación
        station = get_object_or_404(RadioStation, id=station_id)

        # Actualiza el estado de favorito
        station.is_favorite = is_favorite
        station.save() 

        return JsonResponse({"message": "Favorite status updated successfully"})
    except RadioStation.DoesNotExist:
        return JsonResponse({"error": "Station not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
