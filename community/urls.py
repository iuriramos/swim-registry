from django.contrib.auth.views import login, logout_then_login
from django.conf.urls import url
from . import views

app_name='community'

urlpatterns = [
    url(r'^register/$', views.RegisterAccountView.as_view(), name='register'),
    url(r'^profile/$', views.profile_edit, name='profile'),
    url(r'^subscriptions/$', views.subscriptions, name='subscriptions'),
    url(r'^organizations/$', views.organizations_all, name='organizations'),
    #url(r'^organization/$', views.organization_edit, name='organization'),
    #url(r'^organization/new$', views.organization_new, name='organization_new'),
    #url(r'^organizations/$', views.organizations_list, name='organizations'),
]
