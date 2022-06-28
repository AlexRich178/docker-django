from django.urls import path

from measurement.views import SensorViewCreate, SensorViewUpdate, MeasurementView

urlpatterns = [
    path('sensors/', SensorViewCreate.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('sensor/<pk>/', SensorViewUpdate.as_view()),
]
