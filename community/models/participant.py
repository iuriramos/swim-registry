from django.db import models
from swim_registry.models import TimeStampedModel


class Participant(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey('community.ParticipantCategory', related_name='participants')
    image = models.ImageField(upload_to = 'participants/profiles/images/', default = 'participants/profiles/images/none/default.svg')
    reviewed = models.BooleanField(default=False)

    # documents = models.ManyToManyField(ParticipantDocument, related_name='participants')
    # contact_points = models.ManyToManyField(ContactPoint, related_name='participants')

    def __str__(self):
        return self.name
