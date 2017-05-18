from django.db import models


class ImplementationMaturityCategory(models.Model):
    OPERATIONAL = 'OPERATIONAL'
    PROTOTYPE = 'PROTOTYPE'

    CHOICES = (
        OPERATIONAL, 'Operational',
        PROTOTYPE, 'Prototype',
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True)

    class Meta:
        verbose_name = 'implementation maturity category'
        verbose_name_plural = 'implementation maturity categories'

    def __str__(self):
        return self.name
