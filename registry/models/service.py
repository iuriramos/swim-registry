from django.db import models
from .models.data_category import DataCategory
from .models.activity_category import ActivityCategory
from .models.region_category import RegionCategory
from .models.stakeholder_category import StakeholderCategory
from .models.flight_phase_category import FlightPhaseCategory

class Service(models.Model):
    REGISTRATION_STATUS_CHOICES = (
        'DRAFT', 'Draft',
        'VALIDATION', 'Validation',
        'REGISTERED', 'Registered',
    )

    VERSION_CATEGORY_CHOICES = (
        'CURRENT AND SUPPORTED', 'Current and Supported',
        'NON SUPPORTED', 'Non Supported',
        'OBSOLETE BUT SUPPORTED', 'Obsolete but Supported',
        'UPCOMING NOT SUPPORTED', 'Upcoming not Supported',
    )

    IMPLEMENTATION_STATUS_CHOICES = (
        'CURRENT AND SUPPORTED', 'Read for consumption',
        'TERMINATED', 'Terminated',
        'UNDER DEVELOPMENT', 'Under development',
    )

    IMPLEMENTATION_MATURITY_CHOICES = (
        'OPERATIONAL', 'Operational',
        'PROTOTYPE', 'Prototype',
    )

    name = models.CharField(max_length=255, unique=True)
    organization = models.ForeignKey(Participant, related_name='services')
    version = models.CharField(max_length=50, null=False)
    version_category = models.CharField(max_length=50, choices=VERSION_CATEGORY_CHOICES, null=False)
    implementation_status = models.CharField(max_length=50, choices=IMPLEMENTATION_STATUS_CHOICES, null=False)
    implementation_maturity = models.CharField(max_length=50, choices=IMPLEMENTATION_MATURITY_CHOICES, null=False)
    registration_status = models.CharField(max_length=50, choices=REGISTRATION_STATUS_CHOICES, null=False)

    data_categories = models.ManyToManyField(DataCategory, related_name='services')
    activity_categories = models.ManyToManyField(ActivityCategory, related_name='services')
    stakeholders = models.ManyToManyField(StakeholderCategory, related_name='services')
    regions = models.ManyToManyField(RegionCategory, related_name='services')
    flight_phases = models.ManyToManyField(FlightPhaseCategory, related_name='services')

    # service_documentation = models.ManyToManyField(ServiceDocumentation, related_name='services')
    # events = models.ManyToManyField(Event, related_name='services')
    # contact_points = models.ManyToManyField(ContactPoint, related_name='services')
   #  technical_interface = models.OneToOneField(TechnicalInterface, related_name='services')
   #  quality_service_conditions = models.OneToOneField(TechnicalInterface, related_name='services')

    @property
    def organization_name(self):
        return self.organization.name

    def __str__(self):
        return self.name
