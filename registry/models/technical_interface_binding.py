from django.db import models
from swim_registry.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _


class TechnicalInterfaceBindingModel(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    image = models.ImageField(upload_to = 'infrastructure/technical_interface_bindings/images/', default = 'infrastructure/technical_interface_bindings/images/none/default.svg', verbose_name=_('image'))

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class TechnicalInterfaceBindingProfile(TechnicalInterfaceBindingModel):
    infrastructure_profile = models.ForeignKey('registry.InfrastructureProfile', related_name='technical_interface_bindings', verbose_name=_('infrastructure profile'))


class TechnicalInterfaceBindingDescription(TechnicalInterfaceBindingModel):
    infrastructure_description = models.ForeignKey('registry.InfrastructureDescription', related_name='technical_interface_bindings', verbose_name=_('infrastructure description'))

