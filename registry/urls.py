from django.contrib.auth.views import login, logout_then_login
from django.conf.urls import url
from . import views

app_name='registry'

urlpatterns = [
    url(r'^login/$', login, {'template_name':'registry/login.html'}, name='login'),
    url(r'^logout/$', logout_then_login, {'login_url':'/login/'}, name='logout'),
    url(r'^registry/$', views.index, name='index'),
    # url(r'^about/$', views.about, name='about'),
]
