from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=10)

class Route(models.Model):
    user = models.ForeignKey(User)
    start = models.ForeignKey(Location, related_name='start_location')
    finish = models.ForeignKey(Location, related_name='finish_location')

class Point(models.Model):
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    route = models.ForeignKey(Route)
    timestamp = models.DateTimeField(auto_now_add=True)
