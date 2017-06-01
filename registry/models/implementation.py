from django.db import models
from django.utils.translation import ugettext_lazy as _


class ImplementationMaturityCategory(models.Model):
    OPERATIONAL = 'OPERATIONAL'
    PROTOTYPE = 'PROTOTYPE'

    CHOICES = (
        (OPERATIONAL, _('Operational')),
        (PROTOTYPE, _('Prototype')),
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True, verbose_name=_('name'))

    class Meta:
        verbose_name = _('implementation maturity category')
        verbose_name_plural = _('implementation maturity categories')

    def __str__(self):
        return self.name


class ImplementationStatusCategory(models.Model):
    CURRENT_AND_SUPPORTED = 'CURRENT AND SUPPORTED'
    TERMINATED = 'TERMINATED'
    UNDER_DEVELOPMENT = 'UNDER DEVELOPMENT'

    CHOICES = (
        (CURRENT_AND_SUPPORTED, _('Read for consumption')),
        (TERMINATED, _('Terminated')),
        (UNDER_DEVELOPMENT, _('Under development')),
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True, verbose_name=_('name'))

    class Meta:
        verbose_name = _('implementation status category')
        verbose_name_plural = _('implementation status categories')

    def __str__(self):
        return self.name

