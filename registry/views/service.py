from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from registry.models.service import Service
from registry.forms.service import ServiceForm, ServiceSearchForm
from registry.forms.document import ServiceDocumentFormSet
from registry.forms.contact_point import ContactPointServiceFormSet
from .base import get_organization


class ServiceDetailView(DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'registry/service_detail.html'


@login_required
def service_list(request):
    services = Service.objects.filter(reviewed=True)
    form = ServiceSearchForm(request.GET)
    if form.is_valid():
        name = form.cleaned_data['name']
        if name:
            services = services.filter(name__icontains=name)
        description = form.cleaned_data['description']
        if description:
            services = services.filter(description__icontains=description)
        version_category = form.cleaned_data['version_category']
        if version_category:
            services = services.filter(version_category__name__in=version_category)
        implementation_status = form.cleaned_data['implementation_status']
        if implementation_status:
            services = services.filter(implementation_status__name__in=implementation_status)
        implementation_maturity = form.cleaned_data['implementation_maturity']
        if implementation_maturity:
            services = services.filter(implementation_maturity__name__in=implementation_maturity)
        registration_status = form.cleaned_data['registration_status']
        if registration_status:
            services = services.filter(registration_status__name__in=registration_status)
        data_categories = form.cleaned_data['data_categories']
        if data_categories:
            services = services.filter(data_categories__name__in=data_categories)
        activity_categories = form.cleaned_data['activity_categories']
        if activity_categories:
            services = services.filter(activity_categories__name__in=activity_categories)
        stakeholders = form.cleaned_data['stakeholders']
        if stakeholders:
            services = services.filter(stakeholders__name__in=stakeholders)
        regions = form.cleaned_data['regions']
        if regions:
            services = services.filter(regions__name__in=regions)
        flight_phases = form.cleaned_data['flight_phases']
        if flight_phases:
            services = services.filter(flight_phases__name__in=flight_phases)
    return render(request, 'registry/service_list.html', {'form': form, 'services': services})


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

