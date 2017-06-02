from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from registry.models.document import (ServiceDocument, TechnicalInterfaceDocument,
    ReferenceDocument, InfrastructureReferenceDocument, InfrastructureDescriptionDocument,
    DataExchangeFormatServiceDocument, DataExchangeFormatApplicationDocument,
    ApplicationDocument, ParticipantDocument)


@login_required
def reference_document_list(request):
    reference_documents = ReferenceDocument.objects.all()
    infrastructure_reference_documents = InfrastructureReferenceDocument.objects.all()
    return render(request, 'registry/reference_document_list.html', {'reference_documents': reference_documents, 'infrastructure_reference_documents': infrastructure_reference_documents})


class ReferenceDocumentDetailView(DetailView):
    model = ReferenceDocument
    context_object_name = 'document'
    template_name = 'registry/document_detail.html'


class InfrastructureReferenceDocumentDetailView(DetailView):
    model = InfrastructureReferenceDocument
    context_object_name = 'document'
    template_name = 'registry/document_detail.html'


class InfrastructureDescriptionDocumentDetailView(DetailView):
    model = InfrastructureDescriptionDocument
    context_object_name = 'document'
    template_name = 'registry/document_detail.html'


class DataExchangeFormatServiceDocumentDetailView(DetailView):
    model = DataExchangeFormatServiceDocument
    context_object_name = 'document'
    template_name = 'registry/document_detail.html'


class DataExchangeFormatApplicationDocumentDetailView(DetailView):
    model = DataExchangeFormatApplicationDocument
    context_object_name = 'document'
    template_name = 'registry/document_detail.html'


class ApplicationDocumentDetailView(DetailView):
    model = ApplicationDocument
    context_object_name = 'document'
    template_name = 'registry/document_detail.html'


class ParticipantDocumentDetailView(DetailView):
    model = ParticipantDocument
    context_object_name = 'document'
    template_name = 'registry/document_detail.html'


class ServiceDocumentDetailView(DetailView):
    model = ServiceDocument
    context_object_name = 'document'
    template_name = 'registry/document_detail.html'


class ParticipantDocumentDetailView(DetailView):
    model = ParticipantDocument
    context_object_name = 'document'
    template_name = 'registry/document_detail.html'


class TechnicalInterfaceDocumentDetailView(DetailView):
    model = TechnicalInterfaceDocument
    context_object_name = 'document'
    template_name = 'registry/document_detail.html'

