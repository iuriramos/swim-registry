from django.db import models
from django.utils.translation import ugettext_lazy as _
from swim_registry.models import TimeStampedModel


class InfrastructureProfile(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True, verbose_name=_('name'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    version = models.CharField(max_length=50, blank=True, verbose_name=_('version'))
    image = models.ImageField(upload_to = 'infrastructure/profiles/images/', default = 'infrastructure/profiles/images/none/default.svg', verbose_name=_('image'))

    infrastructure_reference_documents = models.ManyToManyField('registry.InfrastructureReferenceDocument', related_name='infrastructure_profiles', verbose_name=_('infrastructure reference documents'))

    # technical_interface_bindings = models.ManyToManyField(TechnicalInterfaceBinding, related_name='infrastructure_profiles')

    class Meta:
        verbose_name=_('infrastructure profile')

    def __str__(self):
        return self.name


class InfrastructureDescription(TimeStampedModel):
    description = models.TextField(blank=True, verbose_name=_('description'))
    version = models.CharField(max_length=50, blank=True, verbose_name=_('version'))
    image = models.ImageField(upload_to = 'infrastructure/infrastructure_description/images/', default = 'infrastructure/infrastructure_description/images/none/default.svg', verbose_name=_('image'))

    infrastructure_reference_documents = models.ManyToManyField('registry.InfrastructureReferenceDocument', related_name='infrastructure_description', blank=True, verbose_name=_('infrastructure reference documents'))

    # infrastructure_documents = models.ManyToManyField(InfrastructureDocument, related_name='infrastructure_description')
    # technical_interface_bindings = models.ManyToManyField(TechnicalInterfaceBinding, related_name='infrastructure_description')

    class Meta:
        verbose_name=_('infrastructure description')

    def __str__(self):
        return self.description
