from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registry.models.data_standard import DataStandard


class DataStandardDetailView(DetailView):
    model = DataStandard
    context_object_name = 'data_standard'
    template_name = 'registry/data_standard_detail.html'
