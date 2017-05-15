from django.db import models


class StakeholderCategory(models.Model):
    AIRPORT_OPERATOR = 'AIRPORT OPERATOR'
    AIRSPACE_USER = 'AIRSPACE USER'
    ANSP = 'ANSP'
    NETWORK_MANAGER  = 'NETWORK MANAGER'

    CHOICES = (
        (AIRPORT_OPERATOR, 'Airport Operator'),
        (AIRSPACE_USER, 'Airspace User'),
        (ANSP, 'ANSP'),
        (NETWORK_MANAGER, 'Network Manager'),
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True)

    class Meta:
        verbose_name = 'stakeholder category'
        verbose_name_plural = 'stakeholder categories'

    def __str__(self):
        return self.name
