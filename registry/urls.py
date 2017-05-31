from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from .views import (index, service, document, end_point, data_standard, data_exchange_format,
        technical_interface_binding)


app_name='registry'

urlpatterns = [
    url(r'^login/$', login, {'template_name':'registry/login.html'}, name='login'),
    url(r'^logout/$', logout_then_login, {'login_url':'/login/'}, name='logout'),
    url(r'^registry/$', index.index_view, name='index'),
    url(r'^organization/services/list/$', service.organization_service_list, name='participant_service_list'),
    url(r'^services/$', login_required(service.ServiceListView.as_view()), name='service_list'),
    url(r'^services/new/$', service.service_new, name='service_new'),
    url(r'^services/(?P<pk>\d+)/detail/$', login_required(service.ServiceDetailView.as_view()), name='service_detail'),
    url(r'^services/(?P<pk>\d+)/edit/$', service.service_edit, name='service_edit'),
    url(r'^services/(?P<pk>\d+)/technical-interface/new/$', service.technical_interface_new, name='technical_interface_new'),
    url(r'^services/(?P<pk>\d+)/technical-interface/edit/$', service.technical_interface_edit, name='technical_interface_edit'),
    url(r'^services/(?P<pk>\d+)/technical-interface/detail/$', login_required(service.TechnicalInterfaceDetailView.as_view()), name='technical_interface_detail'),
    url(r'^technical-interface/(?P<pk>\d+)/infrastructure-description/new/$', service.infrastructure_description_new, name='infrastructure_description_new'),
    url(r'^technical-interface/(?P<pk>\d+)/infrastructure-description/edit/$', service.infrastructure_description_edit, name='infrastructure_description_edit'),
    # url(r'^technical-interface/(?P<pk>\d+)/data-exchange-formats/new/$', service.data_exchange_format_new, name='data_exchange_format_new'),
    url(r'^technical-interface/(?P<pk>\d+)/data-exchange-formats/edit/$', service.data_exchange_formats_edit, name='data_exchange_formats_edit'),
    url(r'^technical-interface/(?P<pk>\d+)/end-points/edit/$', service.end_points_edit, name='end_points_edit'),
    url(r'^service-documents/(?P<pk>\d+)/detail/$', login_required(document.ServiceDocumentDetailView.as_view()), name='service_document_detail'),
    url(r'^infrastructure-reference-documents/(?P<pk>\d+)/detail/$', login_required(document.InfrastructureReferenceDocumentDetailView.as_view()), name='infrastructure_reference_document_detail'),
    url(r'^infrastructure-description-documents/(?P<pk>\d+)/detail/$', login_required(document.InfrastructureDescriptionDocumentDetailView.as_view()), name='infrastructure_description_document_detail'),
    url(r'^service-data-exchange-format-documents/(?P<pk>\d+)/detail/$', login_required(document.DataExchangeFormatServiceDocumentDetailView.as_view()), name='data_exchange_format_service_document_detail'),
    url(r'^technical-interface-documents/(?P<pk>\d+)/detail/$', login_required(document.TechnicalInterfaceDocumentDetailView.as_view()), name='technical_interface_document_detail'),
    url(r'^service-contact-points/(?P<pk>\d+)/detail/$', login_required(service.ServiceContactPointDetailView.as_view()), name='service_contact_point_detail'),
    url(r'^end-points/(?P<pk>\d+)/detail/$', login_required(end_point.EndPointDetailView.as_view()), name='end_point_detail'),
    url(r'^data-standards/(?P<pk>\d+)/detail/$', login_required(data_standard.DataStandardDetailView.as_view()), name='data_standard_detail'),
    url(r'^service-data-exchange-formats/(?P<pk>\d+)/detail/$', login_required(data_exchange_format.DataExchangeFormatServiceDetailView.as_view()), name='service_data_exchange_format_detail'),
    url(r'^infrastructure-profile/technical-interface-binding/(?P<pk>\d+)/detail/$', login_required(technical_interface_binding.TechnicalInterfaceBindingProfileDetailView.as_view()), name='profile_technical_interface_binding_detail'),
    url(r'^infrastructure-description/technical-interface-binding/(?P<pk>\d+)/detail/$', login_required(technical_interface_binding.TechnicalInterfaceBindingDescriptionDetailView.as_view()), name='description_technical_interface_binding_detail'),

    # url(r'^about/$', views.about, name='about'),
]

# ReferenceDocumentDetailView
# DataExchangeFormatApplicationDocumentDetailView
# ApplicationDocumentDetailView
# ParticipantDocumentDetailView
