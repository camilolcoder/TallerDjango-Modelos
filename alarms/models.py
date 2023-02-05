from django.db import models

from measurements.models import Measurement

class Alarms(models.Model):
    measurement = models.ManyToManyField(Measurement, default=None)
    cause = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.cause)
