from django.db import models
from django.utils.translation import ugettext_lazy as _
from swim_registry.models import TimeStampedModel


class TechnicalInterface(TimeStampedModel):
    description = models.TextField(verbose_name=_('description'))
    version = models.CharField(max_length=50, blank=True, verbose_name=_('version'))
    image = models.ImageField(upload_to = 'services/technical_interfaces/images/', default = 'services/technical_interfaces/images/none/default.svg', verbose_name=_('image'))

    infrastructure_reference_documents = models.ManyToManyField('registry.InfrastructureReferenceDocument', related_name='technical_interfaces', blank=True, verbose_name=_('infrastructure reference documents'))
    data_standards = models.ManyToManyField('registry.DataStandard', related_name='technical_interfaces', blank=True, verbose_name=_('data standards'))

    infrastructure_profile = models.ForeignKey('registry.InfrastructureProfile', related_name='technical_interfaces', null=True, blank=True, verbose_name=_('infrastructure profile'))

    service = models.OneToOneField('registry.Service', related_name='technical_interface', verbose_name=_('service'))

    # documents = models.ManyToMany(ServiceDocument, related_name='technical_interfaces')
    # data_exchange_formats = models.ManyToManyField(DataExchangeFormat, related_name='technical_interfaces')
    # end_points = models.ManyToManyField(EndPoint, related_name='technical_interfaces')

    class Meta:
        verbose_name=_('technical interface')

    def __str__(self):
        return _('Technical Interface of {service}').format(service=self.service)

