from django.db import models


class ParticipantCategory(models.Model):
    AIRSPACE_COMPANY = 'AIRSPACE COMPANY'
    RESEARCH_ORGANIZATION = 'RESEARCH ORGANIZATION'
    AIRPORT = 'AIRPORT'
    AERODROME = 'AERODROME'
    RESEARCH_INSTITUTION = 'RESEARCH INSTITUTION'
    PUBLIC_AGENCY = 'PUBLIC AGENCY'
    OTHER = 'OTHER'

    CHOICES = (
        (AIRSPACE_COMPANY, 'Airspace company'),
        (RESEARCH_ORGANIZATION, 'Research Organization'),
        (AIRPORT, 'Airport'),
        (AERODROME, 'Aerodrome'),
        (RESEARCH_INSTITUTION,  'Research Institution'),
        (PUBLIC_AGENCY,  'Public Agency'),
        (OTHER,  'Other'),
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True)

    class Meta:
        verbose_name = 'participant category'
        verbose_name_plural = 'participant categories'

    def __str__(self):
        return self.name
