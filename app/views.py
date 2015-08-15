from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from app.models import Position, Owner, Vehicle
from app.forms import OwnerForm, DateForm
from django.core import serializers

def home(request):
    return render(request, 'home.html')

def get_vehicle(request):
    all_vehicle = Vehicle.objects.filter(owner=request.user.id)
    positions = []
    for s in all_vehicle:
        try:
            position = Position.objects.filter(vehicle=s.id).latest("id")
            positions.append(position)
        except Position.DoesNotExist:
            pass
    data = serializers.serialize('json', positions, use_natural_keys=True)
    return HttpResponse(data, content_type='application/json')

def register(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
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
        form = OwnerForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

def update(request, template_name="update.html"):
    if request.method == "POST":
        form = OwnerForm(data=request.POST, instance=request.user)
        print(request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.instance)
            return redirect("profile")
    else:
        form = OwnerForm(instance=request.user)
    # page_title = _('Edit user names')
    return render_to_response(template_name, locals(),
        context_instance=RequestContext(request))

def profile(request):
    current_user = request.user
    print(current_user.id)
    owner = Owner.objects.get(id=current_user.id)
    owner_vehicles = []
    try:
        vehicles = Vehicle.objects.filter(owner=current_user.id)
        for vehicle in vehicles:
            vehicle_data = {}
            try:
                position = Position.objects.filter(vehicle=vehicle.id).latest("id")
                vehicle_data[vehicle.name] = position.address
            except Position.DoesNotExist:
                pass
            print vehicle_data
            owner_vehicles.append(vehicle_data)
    except Vehicle.DoesNotExist:
         pass

    return render(request, "profile.html", {
        'vehicles': owner_vehicles
    })

def route(request, name):
    vehicle = Vehicle.objects.get(name=name)
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            from_date = form.cleaned_data['from_date']
            to_date = form.cleaned_data['to_date']
            return HttpResponseRedirect('/position/{}/{}/{}'.format(vehicle.id, from_date, to_date))
    else:
        form = DateForm()
    all_positions = []
    try:
        positions = Position.objects.filter(vehicle=vehicle.id)
        latest_position = Position.objects.filter(vehicle=vehicle.id).latest("id")
        latest_position_long = latest_position.long
        latest_position_lat = latest_position.lat
        for position in positions:
            position_array = [position.lat, position.long]
            all_positions.append(position_array)
        print all_positions
    except Position.DoesNotExist:
        positions = None
    return render(request, "route.html", {
        'name': name,
        'positions': positions,
        'all_positions': all_positions,
        'latest_position_long': latest_position_long,
        'latest_position_lat': latest_position_lat,
        'form': form
    })

def position_list(request, vehicle, from_date, to_date):
    """
    Retrieve Positions for selectes time frame
    """
    vehicle = Vehicle.objects.get(pk=vehicle)
    all_positions = []
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            from_date = form.cleaned_data['from_date']
            to_date = form.cleaned_data['to_date']
            return HttpResponseRedirect('/position/{}/{}/{}'.format(vehicle.id, from_date, to_date))
    else:
        form = DateForm()
    try:
        positions = Position.objects.filter(vehicle=vehicle, date__range=(from_date, to_date))
        latest_position = positions.latest("id")
        latest_position_long = latest_position.long
        latest_position_lat = latest_position.lat
        print positions
        for position in positions:
            position_array = [position.lat, position.long]
            all_positions.append(position_array)
        print all_positions
    except Position.DoesNotExist:
        positions = None
        latest_position_long = None
        latest_position_lat = None
    return render(request, "route.html", {
        'form': form,
        'name': vehicle.name,
        'positions': positions,
        'all_positions': all_positions,
        'latest_position_long': latest_position_long,
        'latest_position_lat': latest_position_lat
    })