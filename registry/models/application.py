from django.db import models
from django.utils.translation import ugettext_lazy as _
from swim_registry.models import TimeStampedModel, DocumentModel


class Application(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True, verbose_name=_('name'))
    organization = models.ForeignKey('community.Participant', related_name='applications', verbose_name=_('organization')) # avoid circular imports
    version = models.CharField(max_length=50, verbose_name=_('version'))
    image = models.ImageField(upload_to = 'applications/profiles/images/', default = 'applications/profiles/images/none/default.jpg', verbose_name=_('image'))
    opensource = models.BooleanField(default=False, verbose_name=_('open source'))
    payable = models.BooleanField(default=False, verbose_name=_('payable'))

    version_category = models.ForeignKey('registry.VersionCategory', related_name='applications', verbose_name=_('version category'))
    implementation_status = models.ForeignKey('registry.ImplementationStatusCategory', related_name='applications', verbose_name=_('implementation status'))
    implementation_maturity = models.ForeignKey('registry.ImplementationMaturityCategory', related_name='applications', verbose_name=_('implementation maurity'))
    registration_status = models.ForeignKey('registry.RegistrationStatusCategory', related_name='applications', verbose_name=_('registration status'))

    data_categories = models.ManyToManyField('registry.DataCategory', related_name='applications', verbose_name=_('ATM data categories'))
    activity_categories = models.ManyToManyField('registry.ActivityCategory', related_name='applications', verbose_name=_('ATM activity categories'))
    stakeholders = models.ManyToManyField('registry.StakeholderCategory', related_name='applications', verbose_name=_('stakeholders'))
    regions = models.ManyToManyField('registry.RegionCategory', related_name='applications', verbose_name=_('regions'))
    flight_phases = models.ManyToManyField('registry.FlightPhaseCategory', related_name='applications', verbose_name=_('flight phases'))

    data_standards = models.ManyToManyField('registry.DataStandard', related_name='applications', verbose_name=_('data standards'))
    consumed_services = models.ManyToManyField('registry.Service', related_name='applications', verbose_name=_('consumed services'))

    reviewed = models.BooleanField(default=False, verbose_name=_('reviewed'))
    workflow = models.OneToOneField('registry.Workflow', related_name='application', verbose_name=_('workflow'))
    # files = models.ManyToManyField(ApplicationFile, related_name='applications')

    # data_exchange_formats = models.ManyToManyField(DataExchangeFormat, related_name='applications')
    # documents = models.ManyToManyField(ApplicationDocument, related_name='applications')
    # contact_points = models.ManyToManyField(ContactPoint, related_name='applications')

    ## events = models.ManyToManyField(Event, related_name='applications')
    ##  quality_service_conditions = models.OneToOneField(QualityOfServiceCondition, related_name='applications')


    @property
    def organization_name(self):
        return self.organization.name

    def __str__(self):
        return self.name


class ApplicationFile(DocumentModel):
    file = models.FileField(upload_to = 'applications/files/', null=False)
    image = models.ImageField(upload_to = 'applications/files/images/', default = 'applications/files/images/none/default.jpg', null=True)
    application = models.ForeignKey(Application, related_name='files')
