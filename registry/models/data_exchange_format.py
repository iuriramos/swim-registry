from django.db import models
from swim_registry.models import TimeStampedModel


class DataExchangeFormatModel(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    version = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to = 'infrastructure/data_exchange_formats/profiles/images/', default = 'infrastructure/data_exchange_formats/profiles/images/none/default.svg')

    infrastructure_reference_documents = models.ManyToManyField('registry.InfrastructureReferenceDocument', blank=True)
    # infrastructure_documents = models.ManyToManyField(InfrastructureDocument, related_name='data_exchange_formats')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class DataExchangeFormatService(DataExchangeFormatModel):
    technical_interface = models.ForeignKey('registry.TechnicalInterface', related_name='data_exchange_formats')


class DataExchangeFormatApplication(DataExchangeFormatModel):
    application = models.ForeignKey('registry.Application', related_name='data_exchange_formats')

