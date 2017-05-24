from django.db import models
from swim_registry.models import TimeStampedModel


class EndPoint(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'services/end_points/images/', default = 'services/end_points/images/none/default.svg')
    address = models.URLField(max_length=255, blank=True)
    technical_interface = models.ForeignKey('registry.TechnicalInterface', related_name='end_points')

    def __str__(self):
        return self.name
