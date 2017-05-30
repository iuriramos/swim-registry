from django.db import models
from django.utils.translation import ugettext_lazy as _


class RegionCategory(models.Model):
    BRAZIL = 'BRAZIL'
    AFRICA = 'AFRICA'
    ASIA = 'ASIA'
    EUROPE = 'EUROPE'
    GLOBAL  = 'GLOBAL'
    NORTH_AMERICA = 'NORTH AMERICA'
    OCEANIA = 'OCEANIA'
    SOUTH_AMERICA = 'SOUTH AMERICA'

    CHOICES = (
        (BRAZIL, _('Brazil')),
        (AFRICA, _('Africa')),
        (ASIA, _('Asia')),
        (EUROPE, _('Europe')),
        (GLOBAL , _('Global')),
        (NORTH_AMERICA, _('North America')),
        (OCEANIA, _('Oceania')),
        (SOUTH_AMERICA, _('South America')),
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True)

    class Meta:
        verbose_name = _('region category')
        verbose_name_plural = _('region categories')

    def __str__(self):
        return self.name
