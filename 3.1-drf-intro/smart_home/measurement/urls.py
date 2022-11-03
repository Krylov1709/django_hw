from django.urls import path
from rest_framework.routers import DefaultRouter

from measurement.views import SensorsViewSet, MeasurementViewSet

router_sensors = DefaultRouter()
router_sensors.register('sensors', SensorsViewSet)

router_measurements = DefaultRouter()
router_measurements.register('measurements', MeasurementViewSet)

urlpatterns = [

] + router_sensors.urls + router_measurements.urls
