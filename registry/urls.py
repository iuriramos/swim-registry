from django.contrib.auth.views import login, logout_then_login
from django.conf.urls import url
from .views import index

app_name='registry'

urlpatterns = [
    url(r'^login/$', login, {'template_name':'registry/login.html'}, name='login'),
    url(r'^logout/$', logout_then_login, {'login_url':'/login/'}, name='logout'),
    url(r'^registry/$', index.index_view, name='index'),
    # url(r'^about/$', views.about, name='about'),
]
