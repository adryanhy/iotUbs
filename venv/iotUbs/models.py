from django.db import models

class Equipamentos(models.Model):
    name = models.CharField(max_length=255)
    temperature = models.FloatField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('operational', 'Operational'), ('non-operational', 'Non-operational')])

    def __str__(self):
        return self.name