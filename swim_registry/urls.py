"""swim_registry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
#from .admin import admin_site
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .settings.base import MEDIA_ROOT, MEDIA_URL


urlpatterns = i18n_patterns(
    # url(r'^admin/', include(admin_site.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include('website.urls')),
    url(r'^', include('community.urls')),
    url(r'^', include('registry.urls')),
)
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

admin.site.site_header = _('SWIM Registry Administration')
