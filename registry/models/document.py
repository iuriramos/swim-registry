from django.db import models
from swim_registry.models import DocumentModel


class ReferenceDocument(DocumentModel):
    document = models.FileField(upload_to = 'swim/reference_documents/', null=False)
    image = models.ImageField(upload_to = 'swim/reference_documents/images/', default = 'swim/reference_documents/images/none/default.jpg', null=True)


class InfrastructureReferenceDocument(DocumentModel):
    document = models.FileField(upload_to = 'infrastructure/reference_documents/', null=False)
    image = models.ImageField(upload_to = 'infrastructure/reference_documents/images/', default = 'infrastructure/reference_documents/images/none/default.jpg', null=True)


# class Document(DocumentModel):
#     document = models.FileField(upload_to = 'swim/documents/', null=False)
#     image = models.ImageField(upload_to = 'swim/documents/images/', default = 'swim/documents/images/none/default.jpg', null=True)


class InfrastructureDescriptionDocument(DocumentModel):
    document = models.FileField(upload_to = 'infrastructure/documents/infrastructure_description/', null=False)
    image = models.ImageField(upload_to = 'infrastructure/documents/infrastructure_description/images/', default = 'infrastructure/documents/infrastructure_description/images/none/default.jpg', null=True)
    infrastructure_description = models.ForeignKey('registry.InfrastructureDescription', related_name='documents')


class DataExchangeFormatServiceDocument(DocumentModel):
    document = models.FileField(upload_to = 'infrastructure/documents/data_exchange_formats/', null=False)
    image = models.ImageField(upload_to = 'infrastructure/documents/data_exchange_formats/images/', default = 'infrastructure/documents/data_exchange_formats/images/none/default.jpg', null=True)
    data_exchange_format = models.ForeignKey('registry.DataExchangeFormatService', related_name='documents')


class DataExchangeFormatApplicationDocument(DocumentModel):
    document = models.FileField(upload_to = 'infrastructure/documents/data_exchange_formats/', null=False)
    image = models.ImageField(upload_to = 'infrastructure/documents/data_exchange_formats/images/', default = 'infrastructure/documents/data_exchange_formats/images/none/default.jpg', null=True)
    data_exchange_format = models.ForeignKey('registry.DataExchangeFormatApplication', related_name='documents')


class TechnicalInterfaceDocument(DocumentModel):
    document = models.FileField(upload_to = 'services/technical_interfaces/documents/', null=False)
    image = models.ImageField(upload_to = 'services/technical_interfaces/documents/images/', default = 'services/technical_interfaces/documents/images/none/default.jpg', null=True)
    technical_interface = models.ForeignKey('registry.TechnicalInterface', related_name='documents')


class ServiceDocument(DocumentModel):
    document = models.FileField(upload_to = 'services/documents/', null=False)
    image = models.ImageField(upload_to = 'services/documents/images/', default = 'services/documents/images/none/default.jpg', null=True)
    service = models.ForeignKey('registry.Service', related_name='documents')


class ApplicationDocument(DocumentModel):
    document = models.FileField(upload_to = 'applications/documents/', null=False)
    image = models.ImageField(upload_to = 'applications/documents/images/', default = 'applications/documents/images/none/default.jpg', null=True)
    application = models.ForeignKey('registry.Application', related_name='applications')


class ParticipantDocument(DocumentModel):
    document = models.FileField(upload_to = 'participants/documents/', null=False)
    image = models.ImageField(upload_to = 'participants/documents/images/', default = 'participants/documents/images/none/default.jpg', null=True)
    participant = models.ForeignKey('community.Participant', related_name='documents')

