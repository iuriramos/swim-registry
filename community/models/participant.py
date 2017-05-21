from django.db import models
from swim_registry.models import TimeStampedModel


class Participant(TimeStampedModel):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    category = models.ForeignKey('community.ParticipantCategory', related_name='participants')
    image = models.ImageField(upload_to = 'participants/profiles/images/', default = 'participants/profiles/images/none/default.svg')

    # documents = models.ManyToManyField(ParticipantDocument, related_name='participants')
    # contact_points = models.ManyToManyField(ContactPoint, related_name='participants')

    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
