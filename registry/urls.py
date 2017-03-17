from django.contrib.auth.views import login, logout_then_login
from django.conf.urls import url
from registry import views

urlpatterns = [
    url(r'^register/$', views.RegisterAccountView.as_view(), name='register'),
    url(r'^login/$', login, {'template_name':'login.html'}, name='login'),
    url(r'^logout/$', logout_then_login, {'login_url':'/login/'}, name='logout'),
    url(r'^my-registry/$', views.registry_index, name='registry_index'),
]
