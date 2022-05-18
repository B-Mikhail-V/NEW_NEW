from rest_framework import serializers

# class SensorSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     description = serializers.CharField()
from .models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['pk', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['pk', 'name', 'temperature']


class MeasurementInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']

class SensorDetailSerializer(serializers.ModelSerializer):
    sensor_name = MeasurementInfoSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'sensor_name']