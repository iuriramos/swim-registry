from rest_framework import routers
from django.conf.urls import include
from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from .views import (index, service, document, end_point, data_standard, data_exchange_format,
                    infrastructure, technical_interface, technical_interface_binding, contact_point)

from .serializers.user import UserViewSet
from .serializers.participant import ParticipantViewSet
from .serializers.participant_category import ParticipantCategoryViewSet
from .serializers.service import ServiceViewSet
from .serializers.version_category import VersionCategoryViewSet
from .serializers.implementation import ImplementationStatusCategoryViewSet
from .serializers.implementation import ImplementationMaturityCategoryViewSet
from .serializers.registration_status_category import RegistrationStatusCategoryViewSet
from .serializers.data_category import DataCategoryViewSet
from .serializers.activity_category import ActivityCategoryViewSet
from .serializers.stakeholder_category import StakeholderCategoryViewSet
from .serializers.region_category import RegionCategoryViewSet
from .serializers.flight_phase_category import FlightPhaseCategoryViewSet
from .serializers.technical_interface import TechnicalInterfaceViewSet
from .serializers.technical_interface_binding import TechnicalInterfaceBindingProfileViewSet
from .serializers.infrastructure import InfrastructureProfileViewSet
from .serializers.data_standard import DataStandardViewSet
# from .serializers.data_exchange_format import DataExchangeFormatServiceViewSet
# from .serializers.end_point import EndPointViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('participants', ParticipantViewSet)
router.register('participant-categories', ParticipantCategoryViewSet)
router.register('services', ServiceViewSet)
router.register('version-categories', VersionCategoryViewSet)
router.register('implementation-status-categories', ImplementationStatusCategoryViewSet)
router.register('implementation-maturity-categories', ImplementationMaturityCategoryViewSet)
router.register('registration-status-categories', RegistrationStatusCategoryViewSet)
router.register('data-categories', DataCategoryViewSet)
router.register('activity-categories', ActivityCategoryViewSet)
router.register('stakeholder-categories', StakeholderCategoryViewSet)
router.register('region-categories', RegionCategoryViewSet)
router.register('flight-phase-categories', FlightPhaseCategoryViewSet)
router.register('technical-interfaces', TechnicalInterfaceViewSet)
router.register('data-standards', DataStandardViewSet)
router.register('infrastructure-profiles', InfrastructureProfileViewSet)
router.register('profile-technical-interface-bindings', TechnicalInterfaceBindingProfileViewSet)


app_name='registry'

urlpatterns = [
    url(r'^api/', include(router.urls)),
    
    url(r'^login/$', login, {'template_name':'registry/login.html'}, name='login'),
    url(r'^logout/$', logout_then_login, {'login_url':'/login/'}, name='logout'),
    url(r'^registry/$', index.index_view, name='index'),

    # Service
    url(r'^organization/services/list/$', service.organization_service_list, name='participant_service_list'),
    # url(r'^services/$', login_required(service.ServiceListView.as_view()), name='service_list'),
    url(r'^services/$', service.service_list, name='service_list'),
    url(r'^services/new/$', service.service_new, name='service_new'),
    url(r'^services/(?P<pk>\d+)/detail/$', login_required(service.ServiceDetailView.as_view()), name='service_detail'),
    url(r'^services/(?P<pk>\d+)/edit/$', service.service_edit, name='service_edit'),

    # Technical Interface
    url(r'^services/(?P<pk>\d+)/technical-interface/new/$', technical_interface.technical_interface_new, name='technical_interface_new'),
    url(r'^services/(?P<pk>\d+)/technical-interface/edit/$', technical_interface.technical_interface_edit, name='technical_interface_edit'),
    url(r'^services/(?P<pk>\d+)/technical-interface/detail/$', login_required(technical_interface.TechnicalInterfaceDetailView.as_view()), name='technical_interface_detail'),

    # Infrastructure Description
    url(r'^infrastructure-description/(?P<pk>\d+)/detail/$', login_required(infrastructure.InfrastructureDescriptionDetailView.as_view()), name='infrastructure_description_detail'),
    url(r'^technical-interface/(?P<pk>\d+)/infrastructure-description/new/$', infrastructure.infrastructure_description_new, name='infrastructure_description_new'),
    url(r'^technical-interface/(?P<pk>\d+)/infrastructure-description/edit/$', infrastructure.infrastructure_description_edit, name='infrastructure_description_edit'),

    # Documents
    url(r'^reference-documents/$', document.reference_document_list, name='reference_document_list'),
    url(r'^service-documents/(?P<pk>\d+)/detail/$', login_required(document.ServiceDocumentDetailView.as_view()), name='service_document_detail'),
    url(r'^participant-documents/(?P<pk>\d+)/detail/$', login_required(document.ParticipantDocumentDetailView.as_view()), name='participant_document_detail'),
    url(r'^infrastructure-reference-documents/(?P<pk>\d+)/detail/$', login_required(document.InfrastructureReferenceDocumentDetailView.as_view()), name='infrastructure_reference_document_detail'),
    url(r'^infrastructure-description-documents/(?P<pk>\d+)/detail/$', login_required(document.InfrastructureDescriptionDocumentDetailView.as_view()), name='infrastructure_description_document_detail'),
    url(r'^service-data-exchange-format-documents/(?P<pk>\d+)/detail/$', login_required(document.DataExchangeFormatServiceDocumentDetailView.as_view()), name='data_exchange_format_service_document_detail'),
    url(r'^technical-interface-documents/(?P<pk>\d+)/detail/$', login_required(document.TechnicalInterfaceDocumentDetailView.as_view()), name='technical_interface_document_detail'),

    # Contact Points
    url(r'^service-contact-points/(?P<pk>\d+)/detail/$', login_required(contact_point.ServiceContactPointDetailView.as_view()), name='service_contact_point_detail'),
    url(r'^participant-contact-points/(?P<pk>\d+)/detail/$', login_required(contact_point.ParticipantContactPointDetailView.as_view()), name='participant_contact_point_detail'),

    # End Points
    url(r'^technical-interface/(?P<pk>\d+)/end-points/edit/$', end_point.end_points_edit, name='end_points_edit'),
    url(r'^end-points/(?P<pk>\d+)/detail/$', login_required(end_point.EndPointDetailView.as_view()), name='end_point_detail'),

    # Data Standards
    url(r'^data-standards/(?P<pk>\d+)/detail/$', login_required(data_standard.DataStandardDetailView.as_view()), name='data_standard_detail'),

    # Data Exchange Formats
    url(r'^technical-interface/(?P<pk>\d+)/data-exchange-formats/edit/$', data_exchange_format.data_exchange_formats_edit, name='data_exchange_formats_edit'),
    url(r'^service-data-exchange-formats/(?P<pk>\d+)/detail/$', login_required(data_exchange_format.DataExchangeFormatServiceDetailView.as_view()), name='service_data_exchange_format_detail'),

    # Infrastructure Profile
    url(r'^infrastructure-profile/(?P<pk>\d+)/detail/$', login_required(infrastructure.InfrastructureProfileDetailView.as_view()), name='infrastructure_profile_detail'),

    # Technical Interface Binding
    url(r'^infrastructure-profile/technical-interface-binding/(?P<pk>\d+)/detail/$', login_required(technical_interface_binding.TechnicalInterfaceBindingProfileDetailView.as_view()), name='profile_technical_interface_binding_detail'),
    url(r'^infrastructure-description/technical-interface-binding/(?P<pk>\d+)/detail/$', login_required(technical_interface_binding.TechnicalInterfaceBindingDescriptionDetailView.as_view()), name='description_technical_interface_binding_detail'),

    # Subscriptions
    url(r'^services/(?P<pk>\d+)/detail/toggle-subscription/$', service.service_toggle_subscription, name='service_toggle_subscription'),


    # url(r'^about/$', views.about, name='about'),
]

# ReferenceDocumentDetailView
# DataExchangeFormatApplicationDocumentDetailView
# ApplicationDocumentDetailView
# ParticipantDocumentDetailView
