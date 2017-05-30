from django.db import models
from django.utils.translation import ugettext_lazy as _
from swim_registry.models import TimeStampedModel
from .application import Application
from .service import Service


class ContactPointModel(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    telephone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        abstract = True


class ContactPointService(ContactPointModel):
    image = models.ImageField(upload_to = 'services/contact_points/images/', default = 'services/contact_points/images/none/default.svg', blank=True)
    service = models.ForeignKey('registry.Service', related_name='contact_points')

    class Meta:
        verbose_name = _('service contact point')


class ContactPointApplication(ContactPointModel):
    image = models.ImageField(upload_to = 'applications/contact_points/images/', default = 'applications/contact_points/images/none/default.svg', blank=True)
    application = models.ForeignKey('registry.Application', related_name='contact_points')

    class Meta:
        verbose_name = _('application contact point')


class ContactPointParticipant(ContactPointModel):
    image = models.ImageField(upload_to = 'participants/contact_points/images/', default = 'participants/contact_points/images/none/default.svg', blank=True)
    participant = models.ForeignKey('community.Participant', related_name='contact_points')

    class Meta:
        verbose_name = _('participant contact point')
