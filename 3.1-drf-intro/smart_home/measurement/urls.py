from django.urls import path
from rest_framework.routers import DefaultRouter

from measurement.views import SensorsViewSet, MeasurementsViewSet

router = DefaultRouter()
router.register('sensors', SensorsViewSet)
router.register('measurements', MeasurementsViewSet)

urlpatterns = router.urls
