from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from registry.models.technical_interface import TechnicalInterface
from registry.models.infrastructure import InfrastructureDescription, InfrastructureProfile
from registry.forms.infrastructure import InfrastructureDescriptionForm
from registry.forms.document import InfrastructureDescriptionDocumentFormSet
from registry.forms.technical_interface_binding import TechnicalInterfaceBindingDescriptionFormSet


class InfrastructureDescriptionDetailView(DetailView):
    model = InfrastructureDescription
    context_object_name = 'infrastructure_description'
    template_name = 'registry/infrastructure_description_detail.html'


class InfrastructureProfileDetailView(DetailView):
    model = InfrastructureProfile
    context_object_name = 'infrastructure_profile'
    template_name = 'registry/infrastructure_profile_detail.html'


@login_required
def infrastructure_description_new(request, pk):
    technical_interface = get_object_or_404(TechnicalInterface, pk=pk)
    service = technical_interface.service
    if request.method == 'POST':
        form_infrastructure_description = InfrastructureDescriptionForm(request.POST, request.FILES)
        formset_documents = InfrastructureDescriptionDocumentFormSet(request.POST, request.FILES)
        formset_bindings = TechnicalInterfaceBindingDescriptionFormSet(request.POST, request.FILES)
        if form_infrastructure_description.is_valid() and formset_documents.is_valid() and formset_bindings.is_valid():
            infrastructure_description = form_infrastructure_description.save()
            technical_interface.infrastructure_description = infrastructure_description
            technical_interface.save()
            formset_documents.save()
            formset_bindings.save()
            messages.add_message(request, messages.INFO, _('Infrastructure Description created successfully.'))
            return redirect('registry:infrastructure_description_edit', pk=technical_interface.pk)
    else:
        form_infrastructure_description = InfrastructureDescriptionForm()
        formset_documents = InfrastructureDescriptionDocumentFormSet()
        formset_bindings = TechnicalInterfaceBindingDescriptionFormSet()
    return render(request, 'registry/infrastructure_description_edit.html',
                  {'form_infrastructure_description': form_infrastructure_description,
                    'formset_documents': formset_documents, 'formset_bindings': formset_bindings,
                    'service_pk': service.pk})


@login_required
def infrastructure_description_edit(request, pk):
    technical_interface = get_object_or_404(TechnicalInterface, pk=pk)
    service = technical_interface.service
    infrastructure_description = technical_interface.infrastructure_description
    if request.method == 'POST':
        form_infrastructure_description = InfrastructureDescriptionForm(request.POST, request.FILES, instance=infrastructure_description)
        formset_documents = InfrastructureDescriptionDocumentFormSet(request.POST, request.FILES, instance=infrastructure_description)
        formset_bindings = TechnicalInterfaceBindingDescriptionFormSet(request.POST, request.FILES, instance=infrastructure_description)
        if form_infrastructure_description.is_valid() and formset_documents.is_valid() and formset_bindings.is_valid():
            infrastructure_description = form_infrastructure_description.save()
            technical_interface.infrastructure_description = infrastructure_description
            technical_interface.save()
            formset_documents.save()
            formset_bindings.save()
            messages.add_message(request, messages.INFO, _('Infrastructure Description updated successfully.'))
            return redirect('registry:infrastructure_description_edit', pk=technical_interface.pk)
    else:
        form_infrastructure_description = InfrastructureDescriptionForm(instance=infrastructure_description)
        formset_documents = InfrastructureDescriptionDocumentFormSet(instance=infrastructure_description)
        formset_bindings = TechnicalInterfaceBindingDescriptionFormSet(instance=infrastructure_description)
    return render(request, 'registry/infrastructure_description_edit.html',
                  {'form_infrastructure_description': form_infrastructure_description,
                    'formset_documents': formset_documents, 'formset_bindings': formset_bindings,
                    'service_pk': service.pk})

