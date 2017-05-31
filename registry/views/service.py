from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from registry.models.service import Service
from registry.forms.service import ServiceForm
from registry.forms.document import ServiceDocumentFormSet
from registry.forms.contact_point import ContactPointServiceFormSet
from .base import get_organization


class ServiceListView(ListView):
    model = Service
    context_object_name = 'services'
    queryset = Service.objects.filter(reviewed=True)
    template_name = 'registry/service_list.html'


class ServiceDetailView(DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'registry/service_detail.html'


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

