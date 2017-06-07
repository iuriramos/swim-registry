from django.db import models
from django.utils.translation import ugettext_lazy as _
from swim_registry.models import TimeStampedModel


class Participant(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    website = models.URLField(blank=True, verbose_name=_('website'))
    category = models.ForeignKey('community.ParticipantCategory', related_name='participants', verbose_name=_('participant category'))
    image = models.ImageField(upload_to = 'participants/profiles/images/', default = 'participants/profiles/images/none/default.svg', verbose_name=_('image'))
    reviewed = models.BooleanField(default=False, verbose_name=_('reviewed'))

    # documents = models.ManyToManyField(ParticipantDocument, related_name='participants')
    # contact_points = models.ManyToManyField(ContactPoint, related_name='participants')

    class Meta:
        verbose_name=_('participant')

    def save(self, *args, **kwargs):
        # all services are safe if organization is safe
        super().save(*args, **kwargs)
        if self.reviewed:
            for service in self.services.all():
                service.reviewed = True
                service.save()

    def __str__(self):
        return self.name
