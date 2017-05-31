from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registry.models.technical_interface_binding import TechnicalInterfaceBindingDescription, TechnicalInterfaceBindingProfile


class TechnicalInterfaceBindingProfileDetailView(DetailView):
    model = TechnicalInterfaceBindingProfile
    context_object_name = 'technical_interface_binding'
    template_name = 'registry/technical_interface_binding.html'


class TechnicalInterfaceBindingDescriptionDetailView(DetailView):
    model = TechnicalInterfaceBindingDescription
    context_object_name = 'technical_interface_binding'
    template_name = 'registry/technical_interface_binding.html'


