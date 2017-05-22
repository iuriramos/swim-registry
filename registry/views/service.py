from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from registry.models.service import Service
from .base import get_profile, get_organization
from registry.forms.service import ServiceForm
from registry.forms.technical_interface import TechnicalInterfaceForm
from registry.forms.data_exchange_format import DataExchangeFormatServiceFormSet #######
from registry.forms.document import ServiceDocumentFormSet ############
from registry.forms.infrastructure import InfrastructureDescriptionForm ###########
from registry.forms.document import InfrastructureDescriptionDocumentFormSet ###########
from registry.forms.end_point import EndPointFormSet #################
from registry.forms.technical_interface_binding import TechnicalInterfaceBindingDescriptionFormSet ###########


@login_required
def services_all(request):
    services = Service.objects.filter(reviewed=True)
    return render(request, 'registry/services.html', {'services': services})


@login_required
def services_list(request):
    organization = get_organization(request)
    services = Service.objects.filter(organization=organization)
    return render(request, 'registry/services_list.html', {'services': services})


@login_required
def service_show(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'registry/service_show.html', {'service': service})


@login_required
def service_new(request):
    if request.method == 'POST':
        form_service = ServiceForm(request.POST)
        form_technical_interface = TechnicalInterfaceForm(request.POST)
        formset_data_exchange_format_service = DataExchangeFormatServiceFormSet(request.POST)
        formset_service_document = ServiceDocumentFormSet(request.POST)
        form_infrastructure_description = InfrastructureDescriptionForm(request.POST)
        formset_infrastructure_description_document = InfrastructureDescriptionDocumentFormSet(request.POST)
        formset_end_point = EndPointFormSet(request.POST)
        formset_technical_interface_binding_description = TechnicalInterfaceBindingDescriptionFormSet(request.POST)
        if (form_service.is_valid() and
                form_technical_interface.is_valid() and
                formset_data_exchange_format_service.is_valid() and
                formset_service_document.is_valid() and
                form_infrastructure_description.is_valid() and
                formset_infrastructure_description_document.is_valid() and
                formset_end_point.is_valid() and
                formset_technical_interface_binding_description.is_valid()):
            # everything is valid
            organization = get_organization(request)
            infrastructure_description = form_infrastructure_description.save()
            formset_infrastructure_description_document.save(instance=infrastructure_description)
            formset_end_point.save(instance=infrastructure_description)
            formset_technical_interface_binding_description.save(instance=infrastructure_description)
            technical_interface = form_technical_interface.save(commit=False)
            technical_interface.infrastructure_description = infrastructure_description
            formset_data_exchange_format_service.save(instance=technical_interface)
            formset_service_document.save(instance=technical_interface)
            technical_interface.save()
            service = form_service.save(commit=False)
            service.technical_interface = technical_interface
            service.save()
            messages.add_message(request, messages.INFO, 'Service created successfully')
            return redirect('registry:services_list')
    else:
        form_service = ServiceForm()
        form_technical_interface = TechnicalInterfaceForm()
        formset_data_exchange_format_service = DataExchangeFormatServiceFormSet()
        formset_service_document = ServiceDocumentFormSet()
        form_infrastructure_description = InfrastructureDescriptionForm()
        formset_infrastructure_description_document = InfrastructureDescriptionDocumentFormSet()
        formset_end_point = EndPointFormSet()
        formset_technical_interface_binding_description = TechnicalInterfaceBindingDescriptionFormSet()
    return render(request, 'registry/service_edit.html',
                  {'form_service': form_service,
                  'form_technical_interface': form_technical_interface,
                  'formset_data_exchange_format_service': formset_data_exchange_format_service,
                  'formset_service_document': formset_service_document,
                  'form_infrastructure_description': form_infrastructure_description,
                  'formset_infrastructure_description_document': formset_infrastructure_description_document,
                  'formset_end_point': formset_end_point,
                  'formset_technical_interface_binding_description': formset_technical_interface_binding_description})


# @login_required
# def organization_edit(request):
#     user = request.user
#     profile = get_profile(request)
#     organization = profile.organization
#     if request.method == 'POST':
#         form = OrganizationForm(request.POST, instance=organization)
#         formset_contact_points = ContactPointParticipantFormSet(request.POST, request.FILES, instance=organization)
#         formset_documents = ParticipantDocumentFormSet(request.POST, request.FILES, instance=organization)
#         if form.is_valid() and formset_contact_points.is_valid() and formset_documents.is_valid():
#             form.save()
#             formset_contact_points.save()
#             formset_documents.save()
#             messages.add_message(request, messages.INFO, 'Organization settings updated successfully')
#             return redirect('community:organization')
#     else:
#         form = OrganizationForm(instance=organization)
#         formset_contact_points = ContactPointParticipantFormSet(instance=organization)
#         formset_documents = ParticipantDocumentFormSet(instance=organization)
#     return render(request, 'community/organization_edit.html', {'form': form, 'formset_contact_points': formset_contact_points, 'formset_documents': formset_documents})

