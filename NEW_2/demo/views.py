from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView, \
    RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementInfoSerializer, SensorDetailSerializer, MeasurementSerializer


# @api_view(['GET', 'POST'])
# def demo(request):
#     if request.method == 'GET':
#         sensors = Sensor.objects.all()
#         sens = SensorSerializer(sensors, many=True)
#         return Response(sens.data )
#     if request.method == 'POST':
#         return Response({'status': 'OK'})


# class DemoView(APIView):
#     def get(self, request):
#         sensors = Sensor.objects.all()
#         sens = SensorSerializer(sensors, many=True)
#         return Response(sens.data )
#
#     def post(self, request):
#         return Response({'status': 'OK'})

class DemoView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# Список датчиков и добавление (создание) датчика
class SensorListView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class MeasurementCreate(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class SensorDetailInfo(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

