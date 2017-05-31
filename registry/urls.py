from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from .views import index, service

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
    # url(r'^about/$', views.about, name='about'),
]
