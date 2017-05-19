from django.db import models
from swim_registry.models import TimeStampedModel, DocumentModel
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
from .document import ApplicationDocument
from .contact_point import ContactPoint
from .data import DataStandard, DataExchangeFormat
from .service import Service


class ApplicationFile(DocumentModel):
    file = models.FileField(upload_to = 'applications/files/', null=False)
    image = models.ImageField(upload_to = 'applications/files/images/', default = 'applications/files/images/none/default.jpg', null=True)


class Application(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    organization = models.ForeignKey(Participant, related_name='applications') # avoid circular imports
    version = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to = 'applications/images/profiles/', default = 'applications/images/profiles/none/default.jpg')
    opensource = models.BooleanField(default=False)
    payable = models.BooleanField(default=False)

    version_category = models.ManyToManyField(VersionCategory, related_name='applications')
    implementation_status = models.ManyToManyField(ImplementationStatusCategory, related_name='applications')
    implementation_maturity = models.ManyToManyField(ImplementationMaturityCategory, related_name='applications')
    registration_status = models.ManyToManyField(RegistrationStatusCategory, related_name='applications')

    data_categories = models.ManyToManyField(DataCategory, related_name='applications')
    activity_categories = models.ManyToManyField(ActivityCategory, related_name='applications')
    stakeholders = models.ManyToManyField(StakeholderCategory, related_name='applications')
    regions = models.ManyToManyField(RegionCategory, related_name='applications')
    flight_phases = models.ManyToManyField(FlightPhaseCategory, related_name='applications')

    documents = models.ManyToManyField(ApplicationDocument, related_name='applications')
    contact_points = models.ManyToManyField(ContactPoint, related_name='applications')

    files = models.ManyToManyField(ApplicationFile, related_name='applications')
    data_standards = models.ManyToManyField(DataStandard, related_name='applications')
    data_exchange_formats = models.ManyToManyField(DataExchangeFormat, related_name='applications')
    consumed_services = models.ManyToManyField(Service, related_name='applications')
    # events = models.ManyToManyField(Event, related_name='applications')
    #  quality_service_conditions = models.OneToOneField(QualityOfServiceCondition, related_name='applications')

    @property
    def organization_name(self):
        return self.organization.name

    def __str__(self):
        return self.name

