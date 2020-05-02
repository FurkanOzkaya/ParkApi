from django.db import models


class ParkModel(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    comment = models.CharField(max_length=200, null=True, blank=True)
    created_by = models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        verbose_name = "ParkModel"
        verbose_name_plural = "ParkModels"
