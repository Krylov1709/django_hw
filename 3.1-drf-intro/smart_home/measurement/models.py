from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)


class Measurements(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

