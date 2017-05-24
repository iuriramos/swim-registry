from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from . import views

app_name='community'

urlpatterns = [
    url(r'^register/$', views.RegisterAccountView.as_view(), name='register'),
    url(r'^profile/$', views.profile_edit, name='profile'),
    url(r'^subscriptions/$', views.subscriptions, name='subscriptions'),
    url(r'^organization/edit$', views.organization_edit, name='organization_edit'),
    url(r'^organizations/new$', views.organization_new, name='organization_new'),
    url(r'^organizations/$', login_required(views.OrganizationListView.as_view()), name='organization_list'),
    url(r'^organizations/(?P<pk>\d+)/detail/$', login_required(views.OrganizationDetailView.as_view()), name='organization_detail'),

]
