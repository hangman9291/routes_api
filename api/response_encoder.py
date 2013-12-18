def location_to_json(location):
    return {
        'id' : location.id,
        'name' : location.name,
        'address' : location.address,
        'city' : location.city,
        'state' : location.state,
        'postal_code' : location.postal_code,
    }

def route_to_json(route):
    return {
        'id' : route.id,
        'start' : location_to_json(route.start),
        'finish' : location_to_json(route.finish),
    }

def point_to_json(point):
    return {
        'id;' : point.id,
        'lat' : point.lat,
        'lon' : point.lon,
        'route' : route_to_json(point.route)
    }
