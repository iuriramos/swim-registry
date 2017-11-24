from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from registry.models.end_point import EndPoint
from registry.models.technical_interface import TechnicalInterface
from registry.forms.end_point import EndPointFormSet
from .base import get_organization


class EndPointDetailView(DetailView):
    model = EndPoint
    context_object_name = 'end_point'
    template_name = 'registry/end_point_detail.html'


@login_required
def end_points_edit(request, pk):
    organization = get_organization(request)
    technical_interface = get_object_or_404(TechnicalInterface, pk=pk, service__organization=organization)
    service = technical_interface.service
    if request.method == 'POST':
        formset_end_points = EndPointFormSet(request.POST, request.FILES, instance=technical_interface)
        if formset_end_points.is_valid():
            formset_end_points.save()
            messages.add_message(request, messages.INFO, _('End Points updated successfully.'))
            return redirect('registry:end_points_edit', pk=technical_interface.pk)
    else:
        formset_end_points = EndPointFormSet(instance=technical_interface)
    return render(request, 'registry/end_points_edit.html',
                    {'formset_end_points': formset_end_points,
                     'service_pk': service.pk})
