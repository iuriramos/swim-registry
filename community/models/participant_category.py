from django.db import models
from django.utils.translation import ugettext_lazy as _


class ParticipantCategory(models.Model):
    AIRSPACE_COMPANY = 'AIRSPACE COMPANY'
    RESEARCH_ORGANIZATION = 'RESEARCH ORGANIZATION'
    AIRPORT = 'AIRPORT'
    AERODROME = 'AERODROME'
    RESEARCH_INSTITUTION = 'RESEARCH INSTITUTION'
    PUBLIC_AGENCY = 'PUBLIC AGENCY'
    OTHER = 'OTHER'

    CHOICES = (
        (AIRSPACE_COMPANY, _('Airspace company')),
        (RESEARCH_ORGANIZATION, _('Research Organization')),
        (AIRPORT, _('Airport')),
        (AERODROME, _('Aerodrome')),
        (RESEARCH_INSTITUTION, _('Research Institution')),
        (PUBLIC_AGENCY, _( 'Public Agency')),
        (OTHER, _('Other')),
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True, verbose_name=_('name'))

    class Meta:
        verbose_name = _('participant category')
        verbose_name_plural = _('participant categories')

    def __str__(self):
        return self.name
