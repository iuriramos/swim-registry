from django.db import models
from django.utils.translation import ugettext_lazy as _


class DataCategory(models.Model):
    AERONAUTICAL_INFORMATION = 'AERONAUTICAL INFORMATION'
    METEOROLOGY = 'METEOROLOGY'
    ENVIRONMENT = 'ENVIRONMENT'
    CAPACITY_DEMAND_AND_FLOW = 'CAPACITY DEMAND AND FLOW'
    SURVEILLANCE  = 'SURVEILLANCE'
    OTHER  = 'OTHER'

    CHOICES = (
        (AERONAUTICAL_INFORMATION, _('Aeronautical Information')),
        (METEOROLOGY, _('Meteorology')),
        (ENVIRONMENT, _('Environment')),
        (CAPACITY_DEMAND_AND_FLOW, _('Capacity Demand and Flow')),
        (SURVEILLANCE, _('Surveillance')),
        (OTHER, _('Other')),
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True)

    class Meta:
        verbose_name = _('ATM data category')
        verbose_name_plural = _('ATM data categories')

    def __str__(self):
        return self.name
