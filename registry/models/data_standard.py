from django.db import models
from swim_registry.models import TimeStampedModel


class DataStandard(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    version = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to = 'infrastructure/data_standards/profiles/images/', default = 'infrastructure/data_standards/profiles/images/none/default.svg')

    infrastructure_reference_documents = models.ManyToManyField('registry.InfrastructureReferenceDocument', related_name='data_standards')

    def __str__(self):
        return self.name
