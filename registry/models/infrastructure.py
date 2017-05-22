from django.db import models
from swim_registry.models import TimeStampedModel


class InfrastructureProfile(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)
    version = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to = 'infrastructure/profiles/images/', default = 'infrastructure/profiles/images/none/default.jpg')

    infrastructure_reference_documents = models.ManyToManyField('registry.InfrastructureReferenceDocument', related_name='infrastructure_profiles')
    # technical_interface_bindings = models.ManyToManyField(TechnicalInterfaceBinding, related_name='infrastructure_profiles')

    def __str__(self):
        return self.name


class InfrastructureDescription(TimeStampedModel):
    description = models.TextField(null=True)
    version = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to = 'infrastructure/profiles/images/', default = 'infrastructure/profiles/images/none/default.jpg')

    infrastructure_reference_documents = models.ManyToManyField('registry.InfrastructureReferenceDocument', related_name='infrastructure_description')
    # infrastructure_documents = models.ManyToManyField(InfrastructureDocument, related_name='infrastructure_description')
    # technical_interface_bindings = models.ManyToManyField(TechnicalInterfaceBinding, related_name='infrastructure_description')

    def __str__(self):
        return self.name
