from django.db import models
from swim_registry.models import TimeStampedModel


class DataStandard(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)
    version = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to = 'data/data_standards/images/', default = 'data/data_standards/images/none/default.jpg')

    infrastructure_reference_documents = models.ManyToManyField('registry.InfrastructureReferenceDocument', related_name='data_standards')

    def __str__(self):
        return self.name
