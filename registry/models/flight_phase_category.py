from django.db import models
from django.utils.translation import ugettext_lazy as _


class FlightPhaseCategory(models.Model):
    AIRPORT_RAMP = 'AIRPORT RAMP'
    TAKE_OFF = 'TAKE OFF'
    DEPARTURE = 'DEPARTURE'
    EN_ROUTE = 'EN-ROUTE'
    OCEANIC  = 'OCEANIC'
    ARRIVAL  = 'ARRIVAL'

    CHOICES = (
        (AIRPORT_RAMP, _('Airport (ramp)')),
        (TAKE_OFF, _('Take Off')),
        (DEPARTURE, _('Departure')),
        (EN_ROUTE, _('En-route')),
        (OCEANIC, _('Oceanic')),
        (ARRIVAL, _('Arrival')),
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True)


    class Meta:
        verbose_name = _('flight phase category')
        verbose_name_plural = _('flight phases categories')

    def __str__(self):
        return self.name
