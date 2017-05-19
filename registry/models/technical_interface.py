from django.db import models
from swim_registry.models import TimeStampedModel
from .document import InfrastructureReferenceDocument, ServiceDocument
from .data import DataStandard, DataExchangeFormat
from .infrastructure import InfrastructureProfile, InfrastructureDescription
from .end_point import EndPoint


class TechnicalInterface(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)
    version = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to = 'services/technical_interfaces/images/', default = 'services/technical_interfaces/images/none/default.jpg')

    infrastructure_reference_documents = models.ManyToManyField(InfrastructureReferenceDocument, related_name='technical_interfaces')
    service_documents = models.ManyToManyField(ServiceDocument, related_name='technical_interfaces')
    data_standards = models.ManyToManyField(DataStandard, related_name='technical_interfaces')
    data_exchange_formats = models.ManyToManyField(DataExchangeFormat, related_name='technical_interfaces')
    infrastructure_profile = models.ForeignKey(InfrastructureProfile, related_name='technical_interfaces')
    infrastructure_description = models.ForeignKey(InfrastructureDescription, related_name='technical_interfaces')
    end_points = models.ManyToManyField(EndPoint, related_name='technical_interfaces')

    def __str__(self):
        return self.name

