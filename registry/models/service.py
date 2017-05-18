# from django.db import models
# from .models.data_category import DataCategory
# from .models.activity_category import ActivityCategory
# from .models.region_category import RegionCategory
# from .models.stakeholder_category import StakeholderCategory
# from .models.flight_phase_category import FlightPhaseCategory
# from .models.version_category import VersionCategory
# from .models.regitration_status_category import RegistrationStatusCategory
# from .models.implementation_status_category import ImplementationStatusCategory
# from .models.implementation_maturity_category import ImplementationMaturityCategory


# class Service(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     organization = models.ForeignKey(Participant, related_name='services')
#     version = models.CharField(max_length=50, null=False)

#     version_category = models.ManyToManyField(VersionCategory, related_name='services', null=False)
#     implementation_status = models.ManyToManyField(ImplementationStatusCategory, related_name='services', null=False)
#     implementation_maturity = models.ManyToManyField(ImplementationMaturityCategory, related_name='services', null=False)
#     registration_status = models.ManyToManyField(RegistrationStatusCategory, related_name='services', null=False)

#     data_categories = models.ManyToManyField(DataCategory, related_name='services')
#     activity_categories = models.ManyToManyField(ActivityCategory, related_name='services')
#     stakeholders = models.ManyToManyField(StakeholderCategory, related_name='services')
#     regions = models.ManyToManyField(RegionCategory, related_name='services')
#     flight_phases = models.ManyToManyField(FlightPhaseCategory, related_name='services')

#     # service_documentation = models.ManyToManyField(ServiceDocumentation, related_name='services')
#     # events = models.ManyToManyField(Event, related_name='services')
#     # contact_points = models.ManyToManyField(ContactPoint, related_name='services')
#    #  technical_interface = models.OneToOneField(TechnicalInterface, related_name='services')
#    #  quality_service_conditions = models.OneToOneField(TechnicalInterface, related_name='services')

#     @property
#     def organization_name(self):
#         return self.organization.name

#     def __str__(self):
#         return self.name
