from rest_framework import serializers
from .models import Sensor, Measurement


# TODO: опишите необходимые сериализаторы


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'sensor', 'temperature', 'date']


class SensorDetailSerializer(serializers.ModelSerializer):
    measure = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measure']
