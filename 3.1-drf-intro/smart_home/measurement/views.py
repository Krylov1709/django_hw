from rest_framework.viewsets import ModelViewSet
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementAddSerializer


class SensorsViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementsViewSet(ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementAddSerializer
