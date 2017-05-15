from django.db import models


class RegionCategory(models.Model):
    AFRICA = 'AFRICA'
    ASIA = 'ASIA'
    EUROPE = 'EUROPE'
    GLOBAL  = 'GLOBAL'
    NORTH_AMERICA = 'NORTH AMERICA'
    OCEANIA = 'OCEANIA'
    SOUTH_AMERICA = 'SOUTH AMERICA'

    CHOICES = (
        (AFRICA, 'Africa'),
        (ASIA, 'Asia'),
        (EUROPE, 'Europe'),
        (GLOBAL , 'Global'),
        (NORTH_AMERICA, 'North America'),
        (OCEANIA, 'Oceania'),
        (SOUTH_AMERICA, 'South America'),
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True)

    class Meta:
        verbose_name = 'region category'
        verbose_name_plural = 'region categories'

    def __str__(self):
        return self.name
