from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registry.models.data_exchange_format import DataExchangeFormatService


class DataExchangeFormatServiceDetailView(DetailView):
    model = DataExchangeFormatService
    context_object_name = 'data_exchange_format'
    template_name = 'registry/data_exchange_format_detail.html'
