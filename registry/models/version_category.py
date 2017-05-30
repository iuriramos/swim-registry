from django.db import models
from django.utils.translation import ugettext_lazy as _


class VersionCategory(models.Model):
    CURRENT_AND_SUPPORTED = 'CURRENT AND SUPPORTED'
    NON_SUPPORTED = 'NON SUPPORTED'
    OBSOLETE_BUT_SUPPORTED = 'OBSOLETE BUT SUPPORTED'
    UPCOMING_NOT_SUPPORTED = 'UPCOMING NOT SUPPORTED'

    CHOICES = (
        (CURRENT_AND_SUPPORTED, _('Current and Supported')),
        (NON_SUPPORTED, _('Non Supported')),
        (OBSOLETE_BUT_SUPPORTED, _('Obsolete but Supported')),
        (UPCOMING_NOT_SUPPORTED, _('Upcoming not Supported')),
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True)

    class Meta:
        verbose_name = _('version category')
        verbose_name_plural = _('version categories')

    def __str__(self):
        return self.name
