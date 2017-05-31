from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from registry.models.service import Service
from registry.models.technical_interface import TechnicalInterface
from registry.models.infrastructure import InfrastructureDescription
from registry.models.document import ServiceDocument
from registry.forms.service import ServiceForm
from registry.forms.technical_interface import TechnicalInterfaceForm
from registry.forms.end_point import EndPointFormSet
from registry.forms.contact_point import ContactPointServiceFormSet
from registry.forms.infrastructure import InfrastructureDescriptionForm
from registry.forms.document import ServiceDocumentFormSet, TechnicalInterfaceDocumentFormSet, InfrastructureDescriptionDocumentFormSet, DataExchangeFormatServiceDocumentFormSet
from registry.forms.technical_interface_binding import TechnicalInterfaceBindingDescriptionFormSet
from registry.forms.data_exchange_format import DataExchangeFormatServiceFormSet
from .base import get_profile, get_organization


class ServiceListView(ListView):
    model = Service
    context_object_name = 'services'
    queryset = Service.objects.filter(reviewed=True)
    template_name = 'registry/service_list.html'


class ServiceDetailView(DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'registry/service_detail.html'


class TechnicalInterfaceDetailView(DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'registry/technical_interface_detail.html'


class ServiceDocumentDetailView(DetailView):
    model = ServiceDocument
    context_object_name = 'document'
    template_name = 'registry/service_document_detail.html'


@login_required
def organization_service_list(request):
    organization = get_organization(request)
    services = Service.objects.filter(organization=organization)
    return render(request, 'registry/organization_service_list.html', {'services': services})


@login_required
def service_show(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'registry/service_show.html', {'service': service})


@login_required
def service_new(request):
    organization = get_organization(request)
    if request.method == 'POST':
        form_service = ServiceForm(request.POST, request.FILES)
        formset_documents = ServiceDocumentFormSet(request.POST, request.FILES)
        formset_contact_points = ContactPointServiceFormSet(request.POST, request.FILES)
        if form_service.is_valid() and formset_documents.is_valid() and formset_contact_points.is_valid():
            service = form_service.save(commit=False)
            form_service.save_m2m()
            formset_documents.save()
            formset_contact_points.save()
            service.organization = organization
            service.save()
            messages.add_message(request, messages.INFO, _('Service created successfully. You can now edit servce technical interface.'))
            return redirect('registry:service_edit', pk=service.pk)
    else:
        form_service = ServiceForm()
        formset_documents = ServiceDocumentFormSet()
        formset_contact_points = ContactPointServiceFormSet()
    return render(request, 'registry/service_edit.html',
                  {'form_service': form_service,
                    'formset_documents': formset_documents,
                    'formset_contact_points': formset_contact_points})


@login_required
def service_edit(request, pk):
    organization = get_organization(request)
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form_service = ServiceForm(request.POST, request.FILES, instance=service)
        formset_documents = ServiceDocumentFormSet(request.POST, request.FILES, instance=service)
        formset_contact_points = ContactPointServiceFormSet(request.POST, request.FILES, instance=service)
        if form_service.is_valid() and formset_documents.is_valid() and formset_contact_points.is_valid():
            service = form_service.save(commit=False)
            form_service.save_m2m()
            formset_documents.save()
            formset_contact_points.save()
            service.organization = organization
            service.save()
            messages.add_message(request, messages.INFO, _('Service updated successfully.'))
            return redirect('registry:service_edit', pk=service.pk)
    else:
        form_service = ServiceForm(instance=service)
        formset_documents = ServiceDocumentFormSet(instance=service)
        formset_contact_points = ContactPointServiceFormSet(instance=service)
    return render(request, 'registry/service_edit.html',
                  {'form_service': form_service,
                    'formset_documents': formset_documents,
                    'formset_contact_points': formset_contact_points})


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


@login_required
def end_points_edit(request, pk):
    technical_interface = get_object_or_404(TechnicalInterface, pk=pk)
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


@login_required
def data_exchange_formats_edit(request, pk):
    technical_interface = get_object_or_404(TechnicalInterface, pk=pk)
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
