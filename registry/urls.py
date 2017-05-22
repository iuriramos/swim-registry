from django.contrib.auth.views import login, logout_then_login
from django.conf.urls import url
from .views import index, service

app_name='registry'

urlpatterns = [
    url(r'^login/$', login, {'template_name':'registry/login.html'}, name='login'),
    url(r'^logout/$', logout_then_login, {'login_url':'/login/'}, name='logout'),
    url(r'^registry/$', index.index_view, name='index'),
    url(r'^services/$', service.services_all, name='services_all'),
    url(r'^services/list/$', service.services_list, name='services_list'),
    url(r'^services/new/$', service.service_new, name='service_new'),
    url(r'^services/(?P<pk>\d+)/show/$', service.service_show, name='service_show'),
    # url(r'^services/(?P<pk>\d+)/edit/$', service.service_edit, name='service_edit'),
    # url(r'^about/$', views.about, name='about'),
]
