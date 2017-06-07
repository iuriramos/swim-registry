from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from registry.models.service import Service
from registry.forms.technical_interface import TechnicalInterfaceForm
from registry.forms.document import TechnicalInterfaceDocumentFormSet


class TechnicalInterfaceDetailView(DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'registry/technical_interface_detail.html'


@login_required
def technical_interface_new(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form_technical_interface = TechnicalInterfaceForm(request.POST, request.FILES)
        formset_documents = TechnicalInterfaceDocumentFormSet(request.POST, request.FILES)
        if form_technical_interface.is_valid() and formset_documents.is_valid():
            technical_interface = form_technical_interface.save()
            service.technical_interface = technical_interface
            service.save()
            formset_documents.instance = technical_interface
            formset_documents.save()
            messages.add_message(request, messages.INFO, _('Technical Interface created successfully. You can now edit other technical interface parameters such as infrastructure description, data exchange formats and end points.'))
            return redirect('registry:technical_interface_edit', pk=service.pk)
    else:
        form_technical_interface = TechnicalInterfaceForm()
        formset_documents = TechnicalInterfaceDocumentFormSet()
    return render(request, 'registry/technical_interface_edit.html',
                  {'form_technical_interface': form_technical_interface,
                    'formset_documents': formset_documents,
                    'service_pk': pk})


@login_required
def technical_interface_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    technical_interface = service.technical_interface
    if request.method == 'POST':
        form_technical_interface = TechnicalInterfaceForm(request.POST, request.FILES, instance=technical_interface)
        formset_documents = TechnicalInterfaceDocumentFormSet(request.POST, request.FILES, instance=technical_interface)
        if form_technical_interface.is_valid() and formset_documents.is_valid():
            technical_interface = form_technical_interface.save()
            service.save()
            formset_documents.save()
            messages.add_message(request, messages.INFO, _('Technical Interface updated successfully.'))
            return redirect('registry:technical_interface_edit', pk=service.pk)
    else:
        form_technical_interface = TechnicalInterfaceForm(instance=technical_interface)
        formset_documents = TechnicalInterfaceDocumentFormSet(instance=technical_interface)
    return render(request, 'registry/technical_interface_edit.html',
                  {'form_technical_interface': form_technical_interface,
                    'formset_documents': formset_documents,
                    'service_pk': pk})

