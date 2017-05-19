from django.db import models
from swim_registry.models import TimeStampedModel
from registry.models.document import ParticipantDocument
from registry.models.contact_point import ContactPoint
from .participant_category import ParticipantCategory


class Participant(TimeStampedModel):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    category = models.ForeignKey(ParticipantCategory, related_name='participants')
    image = models.ImageField(upload_to = 'participants/profiles/images/', default = 'participants/profiles/images/none/default.jpg')

    documentations = models.ManyToManyField(ParticipantDocument, related_name='participants')
    contact_points = models.ManyToManyField(ContactPoint, related_name='participants')

    def __str__(self):
        return self.name
