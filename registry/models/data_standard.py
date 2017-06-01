from django.db import models
from django.utils.translation import ugettext_lazy as _
from swim_registry.models import TimeStampedModel


class DataStandard(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True, verbose_name=_('name'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    version = models.CharField(max_length=50, blank=True, verbose_name=_('version'))
    image = models.ImageField(upload_to = 'infrastructure/data_standards/profiles/images/', default = 'infrastructure/data_standards/profiles/images/none/default.svg', verbose_name=_('image'))

    infrastructure_reference_documents = models.ManyToManyField('registry.InfrastructureReferenceDocument', related_name='data_standards', verbose_name=_('infrastructure reference documents'))

    class Meta:
        verbose_name=_('data standard')

    def __str__(self):
        return self.name
