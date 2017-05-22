from django.db import models
from swim_registry.models import TimeStampedModel
from .application import Application
from .service import Service

class ContactPointModel(TimeStampedModel):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    telephone = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    image = models.ImageField(upload_to = 'services/contact_points/images/', default = 'services/contact_points/images/none/default.jpg', null=True)

    class Meta:
        abstract = True


class ContactPointService(ContactPointModel):
    service = models.ForeignKey('registry.Service', related_name='contact_points')

    class Meta:
        verbose_name = 'service contact point'


class ContactPointApplication(ContactPointModel):
    application = models.ForeignKey('registry.Service', related_name='contact_points')

    class Meta:
        verbose_name = 'application contact point'


class ContactPointParticipant(ContactPointModel):
    participant = models.ForeignKey('community.Participant', related_name='contact_points')

    class Meta:
        verbose_name = 'participant contact point'
