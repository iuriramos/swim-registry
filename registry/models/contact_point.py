from django.db import models
from django.utils.translation import ugettext_lazy as _
from swim_registry.models import TimeStampedModel
from .application import Application
from .service import Service


class ContactPointModel(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    telephone = models.CharField(max_length=50, blank=True, verbose_name=_('telephone'))
    email = models.EmailField(blank=True, verbose_name=_('email'))

    class Meta:
        abstract = True


class ContactPointService(ContactPointModel):
    image = models.ImageField(upload_to = 'services/contact_points/images/', default = 'services/contact_points/images/none/default.svg', blank=True, verbose_name=_('image'))
    service = models.ForeignKey('registry.Service', related_name='contact_points', verbose_name=_('service'))

    class Meta:
        verbose_name = _('service contact point')


class ContactPointApplication(ContactPointModel):
    image = models.ImageField(upload_to = 'applications/contact_points/images/', default = 'applications/contact_points/images/none/default.svg', blank=True, verbose_name=_('image'))
    application = models.ForeignKey('registry.Application', related_name='contact_points', verbose_name=_('application'))

    class Meta:
        verbose_name = _('application contact point')


class ContactPointParticipant(ContactPointModel):
    image = models.ImageField(upload_to = 'participants/contact_points/images/', default = 'participants/contact_points/images/none/default.svg', blank=True, verbose_name=_('image'))
    participant = models.ForeignKey('community.Participant', related_name='contact_points', verbose_name=_('participant'))

    class Meta:
        verbose_name = _('participant contact point')
