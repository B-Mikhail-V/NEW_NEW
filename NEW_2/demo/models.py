from django.db import models

# Create your models here.

class Sensor(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.name

class Measurement(models.Model):
    name = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensor_name', verbose_name='Sensor model')
    temperature = models.DecimalField(max_digits=3, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



