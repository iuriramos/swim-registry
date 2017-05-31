from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registry.models.document import (ServiceDocument, TechnicalInterfaceDocument,
    ReferenceDocument, InfrastructureReferenceDocument, InfrastructureDescriptionDocument,
    DataExchangeFormatServiceDocument, DataExchangeFormatApplicationDocument,
    ApplicationDocument, ParticipantDocument)


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


class TechnicalInterfaceDocumentDetailView(DetailView):
    model = TechnicalInterfaceDocument
    context_object_name = 'document'
    template_name = 'registry/document_detail.html'

