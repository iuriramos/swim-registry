from django.db import models
from swim_registry.models import TimeStampedModel
# from .service import Service


class Participant(TimeStampedModel):
    AIRSPACE_COMPANY = 'AIRSPACE COMPANY'
    RESEARCH_ORGANIZATION = 'RESEARCH ORGANIZATION'
    AIRPORT = 'AIRPORT'
    AERODROME = 'AERODROME'
    RESEARCH_INSTITUTION = 'RESEARCH INSTITUTION'
    PUBLIC_AGENCY = 'PUBLIC AGENCY'
    OTHER = 'OTHER'

    PARTICIPANT_CHOICES = (
        (AIRSPACE_COMPANY, 'Airspace company'),
        (RESEARCH_ORGANIZATION, 'Research Organization'),
        (AIRPORT, 'Airport'),
        (AERODROME, 'Aerodrome'),
        (RESEARCH_INSTITUTION,  'Research Institution'),
        (PUBLIC_AGENCY,  'Public Agency'),
        (OTHER,  'Other'),
    )

    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    category = models.CharField(max_length=255, choices=PARTICIPANT_CHOICES, null=False, default=OTHER)
    picture = models.ImageField(upload_to = 'participants/', default = 'participants/none/default.jpg')
    #services = models.ManyToManyField(Service, related_name='participants')
    # applications = models.ManyToManyField(Application, related_name='participants')
    # documentations = models.ManyToManyField(ParticipantDocumentation, related_name='participants')
    # contact_points = models.ManyToManyField(ContactPoint, related_name='participants')

    def __str__(self):
        return self.name
