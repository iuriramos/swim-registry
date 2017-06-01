from django.db import models
from django.utils.translation import ugettext_lazy as _
from swim_registry.models import TimeStampedModel


class EndPoint(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    image = models.ImageField(upload_to = 'services/end_points/images/', default = 'services/end_points/images/none/default.svg', verbose_name=_('image'))
    address = models.URLField(max_length=255, blank=True, verbose_name=_('address'))
    technical_interface = models.ForeignKey('registry.TechnicalInterface', related_name='end_points', verbose_name=_('technical interface'))

    class Meta:
        verbose_name=_('end point')

    def __str__(self):
        return self.name
