from django.db import models
from swim_registry.models import TimeStampedModel


class DataExchangeFormatModel(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)
    version = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to = 'data/data_exchange_formats/images/', default = 'data/data_exchange_formats/images/none/default.jpg')

    infrastructure_reference_documents = models.ManyToManyField('registry.InfrastructureReferenceDocument')
    # infrastructure_documents = models.ManyToManyField(InfrastructureDocument, related_name='data_exchange_formats')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class DataExchangeFormatService(DataExchangeFormatModel):
    technical_interface = models.ForeignKey('registry.TechnicalInterface', related_name='data_exchange_formats')


class DataExchangeFormatApplication(DataExchangeFormatModel):
    application = models.ForeignKey('registry.Application', related_name='data_exchange_formats')

