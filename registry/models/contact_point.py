from django.db import models
from swim_registry.models import TimeStampedModel


class ContactPoint(TimeStampedModel):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    telephone = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    image = models.ImageField(upload_to = 'services/contact_points/images/', default = 'services/contact_points/images/none/default.jpg', null=True)


