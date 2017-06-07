from django.db import models
from django.utils.translation import ugettext_lazy as _
from swim_registry.models import TimeStampedModel
from .registration_status_category import RegistrationStatusCategory


class Service(TimeStampedModel):
    def get_default_registration_status():
        draft = RegistrationStatusCategory.objects.get(name=RegistrationStatusCategory.DRAFT)
        return draft.pk

    name = models.CharField(max_length=255, unique=True, verbose_name=_('name'))
    organization = models.ForeignKey('community.Participant', related_name='services', verbose_name=_('organization'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    version = models.CharField(max_length=50, blank=True, verbose_name=_('version'))
    image = models.ImageField(upload_to = 'services/profiles/images/', default = 'services/profiles/images/none/default.svg', verbose_name=_('image'))

    version_category = models.ForeignKey('registry.VersionCategory', related_name='services', verbose_name=_('version category'))
    implementation_status = models.ForeignKey('registry.ImplementationStatusCategory', related_name='services', verbose_name=_('implementation status'))
    implementation_maturity = models.ForeignKey('registry.ImplementationMaturityCategory', related_name='services', verbose_name=_('implementation maturity'))
    registration_status = models.ForeignKey('registry.RegistrationStatusCategory', default=get_default_registration_status, related_name='services', verbose_name=_('registration status'))

    data_categories = models.ManyToManyField('registry.DataCategory', related_name='services', verbose_name=_('ATM data categories'))
    activity_categories = models.ManyToManyField('registry.ActivityCategory', related_name='services', verbose_name=_('ATM activity categories'))
    stakeholders = models.ManyToManyField('registry.StakeholderCategory', related_name='services', verbose_name=_('stakeholders'))
    regions = models.ManyToManyField('registry.RegionCategory', related_name='services', verbose_name=_('regions'))
    flight_phases = models.ManyToManyField('registry.FlightPhaseCategory', related_name='services', verbose_name=_('flight phases'))

    technical_interface = models.OneToOneField('registry.TechnicalInterface', related_name='service', null=True, verbose_name=_('technical interface'))

    workflow = models.OneToOneField('registry.Workflow', related_name='service', null=True, verbose_name=_('workflow'))
    reviewed = models.BooleanField(default=False, verbose_name=_('reviewed'))

    # documents = models.ManyToManyField(ServiceDocument, related_name='services')
    # contact_points = models.ManyToManyField(ContactPoint, related_name='services')
    ## events = models.ManyToManyField(Event, related_name='services')
    ##  quality_service_conditions = models.OneToOneField(TechnicalInterface, related_name='services')


    class Meta:
        verbose_name=_('service')

    def save(self, *args, **kwargs):
        # reviewed is True if organization is safe
        super().save(*args, **kwargs)
        if self.organization and self.organization.reviewed:
            self.reviewed = True

    @property
    def organization_name(self):
        return self.organization.name

    def __str__(self):
        return self.name
