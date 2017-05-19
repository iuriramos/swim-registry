from django.db import models
from swim_registry.models import TimeStampedModel
from community.models.participant import Participant
from .data_category import DataCategory
from .activity_category import ActivityCategory
from .region_category import RegionCategory
from .stakeholder_category import StakeholderCategory
from .flight_phase_category import FlightPhaseCategory
from .version_category import VersionCategory
from .registration_status_category import RegistrationStatusCategory
from .implementation import ImplementationStatusCategory
from .implementation import ImplementationMaturityCategory
from .document import ServiceDocument
from .technical_interface import TechnicalInterface
from .contact_point import ContactPoint


class Service(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    organization = models.ForeignKey(Participant, related_name='services') # avoid circular imports
    version = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to = 'services/images/profiles/', default = 'services/images/profiles/none/default.jpg')

    version_category = models.ManyToManyField(VersionCategory, related_name='services')
    implementation_status = models.ManyToManyField(ImplementationStatusCategory, related_name='services')
    implementation_maturity = models.ManyToManyField(ImplementationMaturityCategory, related_name='services')
    registration_status = models.ManyToManyField(RegistrationStatusCategory, related_name='services')

    data_categories = models.ManyToManyField(DataCategory, related_name='services')
    activity_categories = models.ManyToManyField(ActivityCategory, related_name='services')
    stakeholders = models.ManyToManyField(StakeholderCategory, related_name='services')
    regions = models.ManyToManyField(RegionCategory, related_name='services')
    flight_phases = models.ManyToManyField(FlightPhaseCategory, related_name='services')

    documents = models.ManyToManyField(ServiceDocument, related_name='services')
    technical_interface = models.OneToOneField(TechnicalInterface, related_name='services')
    contact_points = models.ManyToManyField(ContactPoint, related_name='services')
    # events = models.ManyToManyField(Event, related_name='services')
    #  quality_service_conditions = models.OneToOneField(TechnicalInterface, related_name='services')

    @property
    def organization_name(self):
        return self.organization.name

    def __str__(self):
        return self.name
