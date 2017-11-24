from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from registry.models.technical_interface import TechnicalInterface
from registry.models.data_exchange_format import DataExchangeFormatService
from registry.forms.data_exchange_format import DataExchangeFormatServiceFormSet
from .base import get_organization


class DataExchangeFormatServiceDetailView(DetailView):
    model = DataExchangeFormatService
    context_object_name = 'data_exchange_format'
    template_name = 'registry/data_exchange_format_detail.html'


@login_required
def data_exchange_formats_edit(request, pk):
    organization = get_organization(request)
    technical_interface = get_object_or_404(TechnicalInterface, pk=pk, service__organization=organization)
    service = technical_interface.service
    if request.method == 'POST':
        formset_data_exchange_formats = DataExchangeFormatServiceFormSet(request.POST, request.FILES, instance=technical_interface)
        if formset_data_exchange_formats.is_valid():
            formset_data_exchange_formats.save()
            messages.add_message(request, messages.INFO, _('Data Exchange Formats updated successfully.'))
            return redirect('registry:data_exchange_formats_edit', pk=technical_interface.pk)
    else:
        formset_data_exchange_formats = DataExchangeFormatServiceFormSet(instance=technical_interface)
    return render(request, 'registry/data_exchange_formats_edit.html',
                    {'formset_data_exchange_formats': formset_data_exchange_formats,
                     'service_pk': service.pk})
