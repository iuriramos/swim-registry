from django.db import models
from swim_registry.models import TimeStampedModel


class EndPoint(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to = 'services/end_points/images/', default = 'services/end_points/images/none/default.jpg')
    address = models.URLField(max_length=255, null=True)

    def __str__(self):
        return self.name
