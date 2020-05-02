from gc import get_objects
from math import atan2, cos, radians, sin, sqrt

from app.models import ParkModel
from app.api.serializers import ParkSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

R = 6373.0 # approximate radius of earth in km

class ParkApiList(APIView):
    def get_object(self):
        try:
            return ParkModel.objects.all()
        except ParkModel.DoesNotExist:
            return "NoContent"

    def post(self, request, format=None):
        try:
            lat1 = request.data["latitude"]
            lon1 = request.data["longitude"]
            req_distance = float(request.data["distance"])
            parking_areas = self.get_object()
    
            if type(parking_areas) == str:
                return Response(status=status.HTTP_204_NO_CONTENT)
            
            available_parking_areas = []
            for areas in parking_areas:
                distance = self.get_distance(float(lat1), float(lon1), areas.latitude, areas.longitude)
                if distance < req_distance:
                    available_parking_areas.append(areas)
            serializer = ParkSerializer(available_parking_areas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_distance(self, lat1, lon1, lat2, lon2):
        lat1 = radians(lat1)
        lon1 = radians(lon1)
        lat2 = radians(lat2)
        lon2 = radians(lon2)
        dlon = lon2 - lon1
        
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c

        return distance

class ParkApi(APIView):
    def get_object(self, pk):
        try:
            return ParkModel.objects.get(id=pk)
        except ParkModel.DoesNotExist:
            return "NoContent"

    def get(self, request, pk, format=None):
        parking_area = self.get_object(pk)
        if type(parking_area) == str:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = ParkSerializer(parking_area)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ParkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        parking_area = self.get_object(pk)
        if type(parking_area) == str:
            return Response(status=status.HTTP_204_NO_CONTENT)
        parking_area.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    def put(self, request, pk, format=None):#no need
        parking_area = self.get_object(pk)
        if type(parking_area) == str:
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = ParkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
