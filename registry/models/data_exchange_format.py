from django.db import models
from django.utils.translation import ugettext_lazy as _
from swim_registry.models import TimeStampedModel


class DataExchangeFormatModel(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    version = models.CharField(max_length=50, blank=True, verbose_name=_('version'))
    image = models.ImageField(upload_to = 'infrastructure/data_exchange_formats/profiles/images/', default = 'infrastructure/data_exchange_formats/profiles/images/none/default.svg', verbose_name=_('image'))
    infrastructure_reference_documents = models.ManyToManyField('registry.InfrastructureReferenceDocument', blank=True, verbose_name=_('infrastructure reference documents'))

    # infrastructure_documents = models.ManyToManyField(InfrastructureDocument, related_name='data_exchange_formats')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class DataExchangeFormatService(DataExchangeFormatModel):
    technical_interface = models.ForeignKey('registry.TechnicalInterface', related_name='data_exchange_formats', verbose_name=_('technical interface'))


class DataExchangeFormatApplication(DataExchangeFormatModel):
    application = models.ForeignKey('registry.Application', related_name='data_exchange_formats', verbose_name=_('application'))

