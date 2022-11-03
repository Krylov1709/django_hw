from rest_framework.viewsets import ModelViewSet
from measurement.models import Sensor, Measurements
from measurement.serializers import SensorSerializer, MeasurementSerializer


class SensorsViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementViewSet(ModelViewSet):
    queryset = Measurements.objects.all()
    serializer_class = MeasurementSerializer
