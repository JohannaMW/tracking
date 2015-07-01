from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from app.api.serializers import *
from django.views.decorators.csrf import csrf_exempt
from datetime import tzinfo, timedelta, datetime

ZERO = timedelta(0)


class UTC(tzinfo):
    def utcoffset(self, dt):
        return ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return ZERO


utc = UTC()


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


@csrf_exempt
def driver_check(request, rfid, scooter_id):
    try:
        Driver.objects.get(rfid=rfid)
        Scooter.objects.get(pk=scooter_id)
    except Driver.DoesNotExist:
        return HttpResponse(status=404)
    scooter = Scooter.objects.get(pk=scooter_id)
    driver = Driver.objects.get(rfid=rfid)
    if scooter.in_use:
        scooter.in_use = False
        scooter.save(update_fields=["in_use"])
        trip = Trip.objects.filter(driver=driver, scooter=scooter).order_by('-pk')[0]
        now = datetime.now(utc)
        trip.end = now
        length = trip.start - trip.end
        print length
        length_in_minutes = length.seconds / 60
        trip.length = length_in_minutes
        trip.save(update_fields=["end", "length"])
    else:
        scooter.in_use = True
        scooter.save(update_fields=["in_use"])
        now = datetime.now(utc)
        Trip.objects.create(start=now, driver=driver, scooter=scooter)
    return HttpResponse(status=200)


class ScooterViewSet(viewsets.ModelViewSet):
    queryset = Scooter.objects.all()
    serializer_class = ScooterSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
