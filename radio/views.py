from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RadioStation
from .serializers import RadioStationSerializer

class RadioStationList(APIView):
    def get(self, request):
        stations = RadioStation.objects.all()
        serializer = RadioStationSerializer(stations, many=True, context={'request': request})
        return Response(serializer.data)
