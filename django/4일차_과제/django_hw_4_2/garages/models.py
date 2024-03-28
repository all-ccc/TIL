from django.db import models

# Create your models here.
class Garage(models.Model):
    location = models.CharField(max_length=200)
    capacity = models.IntegerField(default=0)
    is_parking_available = models.BooleanField(default=True)
    opening_time = models.TimeField(auto_now=False)
    closing_time = models.TimeField(auto_now=False)