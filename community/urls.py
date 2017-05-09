from django.contrib.auth.views import login, logout_then_login
from django.conf.urls import url
from . import views

app_name='community'

urlpatterns = [
    url(r'^register/$', views.RegisterAccountView.as_view(), name='register'),

]
