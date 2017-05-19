from django.contrib import admin
from .models.subscription_content_type import SubscriptionContentType
from .models.region_category import RegionCategory
from .models.data_category import DataCategory
from .models.activity_category import ActivityCategory
from .models.flight_phase_category import FlightPhaseCategory
from .models.stakeholder_category import StakeholderCategory
from .models.registration_status_category import RegistrationStatusCategory
from .models.version_category import VersionCategory
from .models.implementation import ImplementationStatusCategory, ImplementationMaturityCategory
from .models.service import Service
from .models.application import Application


admin.site.register(RegionCategory)
admin.site.register(StakeholderCategory)
admin.site.register(DataCategory)
admin.site.register(ActivityCategory)
admin.site.register(FlightPhaseCategory)
admin.site.register(SubscriptionContentType)
admin.site.register(RegistrationStatusCategory)
admin.site.register(VersionCategory)
admin.site.register(ImplementationStatusCategory)
admin.site.register(ImplementationMaturityCategory)
admin.site.register(Service)
admin.site.register(Application)
