from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app.models import Position
from app.forms import DriverForm
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

def register(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password1"]
            form.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("home")
    else:
        form = DriverForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

