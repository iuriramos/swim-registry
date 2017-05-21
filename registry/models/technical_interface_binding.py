from django.db import models
from swim_registry.models import TimeStampedModel


class TechnicalInterfaceBindingModel(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to = 'infrastructure/technical_interface_bindings/images/', default = 'infrastructure/technical_interface_bindings/images/none/default.jpg')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class TechnicalInterfaceBindingProfile(TechnicalInterfaceBindingModel):
    infrastructure_profile = models.ForeignKey('registry.InfrastructureProfile', related_name='technical_interface_bindings')


class TechnicalInterfaceBindingDescription(TechnicalInterfaceBindingModel):
    infrastructure_description = models.ForeignKey('registry.InfrastructureDescription', related_name='technical_interface_bindings')
