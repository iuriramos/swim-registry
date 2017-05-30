from django.db import models
from django.utils.translation import ugettext_lazy as _
from swim_registry.models import TimeStampedModel


class TechnicalInterface(TimeStampedModel):
    description = models.TextField()
    version = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to = 'services/technical_interfaces/images/', default = 'services/technical_interfaces/images/none/default.svg')

    infrastructure_reference_documents = models.ManyToManyField('registry.InfrastructureReferenceDocument', related_name='technical_interfaces', blank=True)
    data_standards = models.ManyToManyField('registry.DataStandard', related_name='technical_interfaces', blank=True)

    infrastructure_profile = models.ForeignKey('registry.InfrastructureProfile', related_name='technical_interfaces', null=True, blank=True)

    infrastructure_description = models.OneToOneField('registry.InfrastructureDescription', related_name='technical_interface', null=True, blank=True)

    # documents = models.ManyToMany(ServiceDocument, related_name='technical_interfaces')
    # data_exchange_formats = models.ManyToManyField(DataExchangeFormat, related_name='technical_interfaces')
    # end_points = models.ManyToManyField(EndPoint, related_name='technical_interfaces')

    def __str__(self):
        return _('Technical Interface of {service}').format(service=self.service)

