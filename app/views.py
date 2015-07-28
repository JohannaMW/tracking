from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from app.models import Position, Driver, Trip, Scooter
from app.forms import DriverForm
import datetime
from datetime import date, timedelta
from django.core import serializers

def home(request):
    return render(request, 'home.html')

def get_scooter(request):
    all_scooter = Scooter.objects.all()
    positions = []
    for s in all_scooter:
        position = Position.objects.filter(scooter=s.id).order_by('-time')[0]
        print position
        positions.append(position)
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
                    return redirect("profile")
    else:
        form = DriverForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

def update(request, template_name="update.html"):
    if request.method == "POST":
        form = DriverForm(data=request.POST, instance=request.user)
        print(request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.instance)
            return redirect("profile")
    else:
        form = DriverForm(instance=request.user)
    # page_title = _('Edit user names')
    return render_to_response(template_name, locals(),
        context_instance=RequestContext(request))

def profile(request):
    current_user = request.user
    print(current_user.id)
    driver = Driver.objects.get(id=current_user.id)
    try:
        trips = Trip.objects.filter(driver=current_user.id)
    except Trip.DoesNotExist:
        trips = None

    return render(request, "profile.html", {
        'driver': driver,
        'trips': trips
    })

