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
from .models.workflow import Workflow
from .models.technical_interface import TechnicalInterface
from .models.technical_interface_binding import TechnicalInterfaceBindingProfile, TechnicalInterfaceBindingDescription
from .models.infrastructure import InfrastructureProfile, InfrastructureDescription
from .models.document import InfrastructureReferenceDocument, ReferenceDocument
from .models.data_standard import DataStandard
from .models.data_exchange_format import DataExchangeFormatService, DataExchangeFormatApplication
from .models.contact_point import ContactPointService, ContactPointParticipant
from .models.review_request import ReviewRequestService
from .forms.review_request import ReviewRequestServiceForm, ReviewRequestServiceAdminForm


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
admin.site.register(TechnicalInterface)
admin.site.register(Application)
admin.site.register(ReferenceDocument)
admin.site.register(InfrastructureReferenceDocument)
admin.site.register(DataStandard)
admin.site.register(Workflow)


class TechnicalInterfaceBindingProfileInline(admin.TabularInline):
    model = TechnicalInterfaceBindingProfile

class InfrastructureProfileAdmin(admin.ModelAdmin):
    inlines = [
        TechnicalInterfaceBindingProfileInline,
    ]
admin.site.register(InfrastructureProfile, InfrastructureProfileAdmin)


class ReviewRequestServiceAdmin(admin.ModelAdmin):
    form = ReviewRequestServiceAdminForm
admin.site.register(ReviewRequestService, ReviewRequestServiceAdmin)

