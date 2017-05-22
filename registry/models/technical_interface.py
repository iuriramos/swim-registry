from django.db import models
from swim_registry.models import TimeStampedModel


class TechnicalInterface(TimeStampedModel):
    description = models.TextField(null=True)
    version = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to = 'services/technical_interfaces/images/', default = 'services/technical_interfaces/images/none/default.svg')

    infrastructure_reference_documents = models.ManyToManyField('registry.InfrastructureReferenceDocument', related_name='technical_interfaces')
    data_standards = models.ManyToManyField('registry.DataStandard', related_name='technical_interfaces')

    infrastructure_profile = models.ForeignKey('registry.InfrastructureProfile', related_name='technical_interfaces')
    infrastructure_description = models.OneToOneField('registry.InfrastructureDescription', related_name='technical_interface', null=True)

    # documents = models.ManyToMany(ServiceDocument, related_name='technical_interfaces')
    # data_exchange_formats = models.ManyToManyField(DataExchangeFormat, related_name='technical_interfaces')
    # end_points = models.ManyToManyField(EndPoint, related_name='technical_interfaces')

    def __str__(self):
        return 'Technical Interface of {service}'.format(service=self.service)

