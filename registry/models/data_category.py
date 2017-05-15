from django.db import models


class DataCategory(models.Model):
    AERONAUTICAL_INFORMATION = 'AERONAUTICAL INFORMATION'
    METEOROLOGY = 'METEOROLOGY'
    ENVIRONMENT = 'ENVIRONMENT'
    CAPACITY_DEMAND_AND_FLOW = 'CAPACITY DEMAND AND FLOW'
    SURVEILLANCE  = 'SURVEILLANCE'
    OTHER  = 'OTHER'

    CHOICES = (
        (AERONAUTICAL_INFORMATION, 'Aeronautical Information'),
        (METEOROLOGY, 'Meteorology'),
        (ENVIRONMENT, 'Environment'),
        (CAPACITY_DEMAND_AND_FLOW, 'Capacity Demand and Flow'),
        (SURVEILLANCE, 'Surveillance'),
        (OTHER, 'Other'),
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True)

    class Meta:
        verbose_name = 'ATM data category'
        verbose_name_plural = 'ATM data categories'

    def __str__(self):
        return self.name
