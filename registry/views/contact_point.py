from django.views.generic.detail import DetailView
from registry.models.contact_point import ContactPointService


class ServiceContactPointDetailView(DetailView):
    model = ContactPointService
    context_object_name = 'contact_point'
    template_name = 'registry/contact_point_detail.html'
