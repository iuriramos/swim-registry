from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from . import views


app_name='community'

urlpatterns = [
    url(r'^register/$', views.RegisterAccountView.as_view(), name='register'),
    url(r'^profile/$', views.profile_edit, name='profile'),
    url(r'^subscriptions/$', views.subscriptions, name='subscriptions'),
    url(r'^organization/edit$', views.participant_edit, name='participant_edit'),
    url(r'^organizations/new$', views.participant_new, name='participant_new'),
    url(r'^organizations/$', login_required(views.ParticipantListView.as_view()), name='participant_list'),
    url(r'^organizations/(?P<pk>\d+)/detail/$', login_required(views.ParticipantDetailView.as_view()), name='participant_detail'),

    # Subscriptions
    url(r'^organizations/(?P<pk>\d+)/detail/toggle-subscription/$', views.participant_toggle_subscription, name='participant_toggle_subscription'),

]
