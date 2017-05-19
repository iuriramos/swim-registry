from django.db import models
from swim_registry.models import TimeStampedModel


class TechnicalInterfaceBinding(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to = 'infrastructure/technical_interface_bindings/images/', default = 'infrastructure/technical_interface_bindings/images/none/default.jpg')

    def __str__(self):
        return self.name
