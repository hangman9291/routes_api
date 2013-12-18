from django.contrib.auth import authenticate, login
from api.models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import json
from response_encoder import location_to_json, route_to_json, point_to_json

@csrf_exempt
def signup(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    if username and email and password:
        user = User.objects.create_user(username, email, password)
        return HttpResponse('success')
    else:
        return HttpResponse(status=400, content='Bad request')

@csrf_exempt
def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password:
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponse('success')
        else:
            return HttpResponse(status=401, content='Bad credentials')
    else:
        return HttpResponse(status=400, content='Bad request')

@csrf_exempt
@login_required
def locations(request):
    if request.method == 'GET':
        locations_array = []
        locations = Location.objects.filter(user=request.user)
        for location in locations:
            locations_array.append(location_to_json(location))
        return HttpResponse(json.dumps(locations_array))
    elif request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postal_code = request.POST.get('postal_code')
        if name and address and city and state and postal_code:
            location = Location(user=request.user, name=name, address=address, city=city, state=state, postal_code=postal_code)
            location.save()
            return HttpResponse('ok')
        else:
            return HttpResponse(status=400, content='Bad request')
    else:
        return HttpResponse(status=405, content='Method not supported')

@csrf_exempt
@login_required
def route(request):
    if request.method == 'GET':
        routes_list = []
        routes = Route.objects.filter(user=request.user)
        for route in routes:
            routes_list.append(route_to_json(route))
        return HttpResponse(json.dumps(routes_list))
    elif request.method == 'POST':
        start_id = request.POST.get('start_id')
        finish_id = request.POST.get('finish_id')
        if start_id and finish_id:
            start = Location.objects.get(id=start_id)
            finish = Location.objects.get(id=finish_id)
            route = Route(user=request.user, start=start, finish=finish)
            route.save()
            return HttpResponse('ok')
        else:
            return HttpResponse(status=400, content='Bad request')
    else:
        return HttpResponse(status=405, content='Method not supported')

@csrf_exempt
@login_required
def point(request):
    if request.method == 'POST':
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')
        route_id = request.POST.get('route_id')
        if lat and lon and route_id:
            route = Route.objects.get(route__id=route_id)
            point = Point(lat=lat, lon=lon, route=route)
            point.save()
            return HttpResponse('ok')
        else:
            return HttpResponse(status=400, content='Bad request')
    else:
        return HttpResponse(status=405, content='Method not supported')

@csrf_exempt
@login_required
def point_id(request):
    if request.method == 'POST':
        route_id = request.POST.get('route_id')
        if route_id:
            points_list = []
            points = Point.objects.filter(id=route_id)
            for point in points:
                points_list.append(point)
            return HttpResponse(json.dumps(points_list))
        else:
            return HttpResponse(status=400, content='Bad request')
    else:
        return HttpResponse(status=405, content='Method not supported')

