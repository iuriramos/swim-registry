from django.db import models
from swim_registry.models import DocumentModel


class ReferenceDocument(DocumentModel):
    document = models.FileField(upload_to = 'swim/reference_documents/', null=False)
    image = models.ImageField(upload_to = 'swim/reference_documents/images/', default = 'swim/reference_documents/images/none/default.jpg', null=True)


class Document(DocumentModel):
    document = models.FileField(upload_to = 'swim/documents/', null=False)
    image = models.ImageField(upload_to = 'swim/documents/images/', default = 'swim/documents/images/none/default.jpg', null=True)


class InfrastructureReferenceDocument(DocumentModel):
    document = models.FileField(upload_to = 'infrastructure/reference_documents/', null=False)
    image = models.ImageField(upload_to = 'infrastructure/reference_documents/images/', default = 'infrastructure/reference_documents/images/none/default.jpg', null=True)


class InfrastructureDocument(DocumentModel):
    document = models.FileField(upload_to = 'infrastructure/documents/', null=False)
    image = models.ImageField(upload_to = 'infrastructure/documents/images/', default = 'infrastructure/documents/images/none/default.jpg', null=True)


class ServiceDocument(DocumentModel):
    document = models.FileField(upload_to = 'services/documents/', null=False)
    image = models.ImageField(upload_to = 'services/documents/images/', default = 'services/documents/images/none/default.jpg', null=True)


class ApplicationDocument(DocumentModel):
    document = models.FileField(upload_to = 'applications/documents/', null=False)
    image = models.ImageField(upload_to = 'applications/documents/images/', default = 'applications/documents/images/none/default.jpg', null=True)


class ParticipantDocument(DocumentModel):
    document = models.FileField(upload_to = 'participants/documents/', null=False)
    image = models.ImageField(upload_to = 'participants/documents/images/', default = 'participants/documents/images/none/default.jpg', null=True)

