from django.db import models


class FlightPhaseCategory(models.Model):
    AIRPORT_RAMP = 'AIRPORT RAMP'
    TAKE_OFF = 'TAKE OFF'
    DEPARTURE = 'DEPARTURE'
    EN_ROUTE = 'EN-ROUTE'
    OCEANIC  = 'OCEANIC'
    ARRIVAL  = 'ARRIVAL'

    CHOICES = (
        (AIRPORT_RAMP, 'Airport (ramp)'),
        (TAKE_OFF, 'Take Off'),
        (DEPARTURE, 'Departure'),
        (EN_ROUTE, 'En-route'),
        (OCEANIC, 'Oceanic'),
        (ARRIVAL, 'Arrival'),
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True)


    class Meta:
        verbose_name = 'flight phase category'
        verbose_name_plural = 'flight phases categories'

    def __str__(self):
        return self.name
