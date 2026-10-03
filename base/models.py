from django.db import models

# Create your models here.
class flightmodel(models.Model):
    flight_company = models.CharField(max_length=100)
    flight_name = models.CharField(max_length=100)
    flight_no = models.IntegerField(max_length=50)
    form = models.CharField(max_length=50)
    to = models.CharField(max_length=50)


