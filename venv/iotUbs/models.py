from django.db import models
from django.utils import timezone

class Equipamentos(models.Model):
    name = models.CharField(max_length=255)
    temperature = models.FloatField()
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    status = models.CharField(max_length=50, choices=[('operational', 'Operational'), ('non-operational', 'Non-operational')])

    def __str__(self):
        return self.name
    

class EquipmentLog(models.Model):
    equipment_name = models.CharField(max_length=255)
    temperature = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.CharField(max_length=50)
    added_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Log - {self.equipment_name} added on {self.added_at}"
    