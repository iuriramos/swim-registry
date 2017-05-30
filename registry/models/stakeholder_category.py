from django.db import models
from django.utils.translation import ugettext_lazy as _


class StakeholderCategory(models.Model):
    AIRPORT_OPERATOR = 'AIRPORT OPERATOR'
    AIRSPACE_USER = 'AIRSPACE USER'
    ANSP = 'ANSP'
    NETWORK_MANAGER  = 'NETWORK MANAGER'

    CHOICES = (
        (AIRPORT_OPERATOR, _('Airport Operator')),
        (AIRSPACE_USER, _('Airspace User')),
        (ANSP, _('ANSP')),
        (NETWORK_MANAGER, _('Network Manager')),
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True)

    class Meta:
        verbose_name = _('stakeholder category')
        verbose_name_plural = _('stakeholder categories')

    def __str__(self):
        return self.name
