from django.http import HttpResponse
from rest_framework import viewsets
from app.api.serializers import *
from geopy.geocoders import Nominatim

geolocator = Nominatim()

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

def post_long_lat(request, long, lat, vehicle_id):
    #arse string arguments to float
    longitude = float(long)
    latitude = float(lat)
    if request.method == 'GET':
        try:
            Vehicle.objects.get(pk=vehicle_id)
        except Vehicle.DoesNotExist:
            return HttpResponse(status=404)
        vehicle = Vehicle.objects.get(pk=vehicle_id)
        #save only if position differs from previous
        try:
            last_position = Position.objects.filter(vehicle=vehicle_id).latest("id")
            if abs(latitude) == abs(last_position.lat):
                vehicle.in_use = "false"
            else:
                vehicle.in_use = "true"
                geo = "{}, {}".format(lat, long)
                location = geolocator.reverse(geo)
                Position.objects.create(long=longitude, lat=latitude, vehicle=vehicle, address=location)
        except Position.DoesNotExist:
            Position.objects.create(long=long, lat=lat, vehicle=vehicle)

        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
