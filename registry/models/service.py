from django.db import models
from swim_registry.models import TimeStampedModel


class Service(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    organization = models.ForeignKey('community.Participant', related_name='services')
    description = models.TextField(blank=True)
    version = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to = 'services/profiles/images/', default = 'services/profiles/images/none/default.svg')

    version_category = models.ForeignKey('registry.VersionCategory', related_name='services')
    implementation_status = models.ForeignKey('registry.ImplementationStatusCategory', related_name='services')
    implementation_maturity = models.ForeignKey('registry.ImplementationMaturityCategory', related_name='services')
    registration_status = models.ForeignKey('registry.RegistrationStatusCategory', related_name='services')

    data_categories = models.ManyToManyField('registry.DataCategory', related_name='services')
    activity_categories = models.ManyToManyField('registry.ActivityCategory', related_name='services')
    stakeholders = models.ManyToManyField('registry.StakeholderCategory', related_name='services')
    regions = models.ManyToManyField('registry.RegionCategory', related_name='services')
    flight_phases = models.ManyToManyField('registry.FlightPhaseCategory', related_name='services')

    technical_interface = models.OneToOneField('registry.TechnicalInterface', related_name='service', null=True)

    reviewed = models.BooleanField(default=False)
    workflow = models.OneToOneField('registry.Workflow', related_name='service', null=True)

    # documents = models.ManyToManyField(ServiceDocument, related_name='services')
    # contact_points = models.ManyToManyField(ContactPoint, related_name='services')
    ## events = models.ManyToManyField(Event, related_name='services')
    ##  quality_service_conditions = models.OneToOneField(TechnicalInterface, related_name='services')


    @property
    def organization_name(self):
        return self.organization.name

    def __str__(self):
        return self.name
