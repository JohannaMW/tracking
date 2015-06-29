from django.http import HttpResponse
from django.shortcuts import render
from app.models import Position
import datetime
import json
from django.core import serializers

now = datetime.datetime.now()

def home(request):
    return render(request, 'home.html')

def get_scooter(request):
    current_date_time = now.isoformat()
    #scooter = Scooter.objects.get(time=current_date_time)
    positions = Position.objects.all()
    data = serializers.serialize('json', positions, use_natural_keys=True)
    return HttpResponse(data, content_type='application/json')