from django.db import models
from django.utils.translation import ugettext_lazy as _
from swim_registry.models import DocumentModel


class ReferenceDocument(DocumentModel):
    document = models.FileField(upload_to = 'swim/reference_documents/', blank=True, verbose_name=_('document'))
    image = models.ImageField(upload_to = 'swim/reference_documents/images/', default = 'swim/reference_documents/images/none/default.svg', blank=True, verbose_name=_('image'))


class InfrastructureReferenceDocument(DocumentModel):
    document = models.FileField(upload_to = 'infrastructure/reference_documents/', blank=True, verbose_name=_('document'))
    image = models.ImageField(upload_to = 'infrastructure/reference_documents/images/', default = 'infrastructure/reference_documents/images/none/default.svg', blank=True, verbose_name=_('image'))


# class Document(DocumentModel):
#     document = models.FileField(upload_to = 'swim/documents/', blank=True)
#     image = models.ImageField(upload_to = 'swim/documents/images/', default = 'swim/documents/images/none/default.svg', blank=True)


class InfrastructureDescriptionDocument(DocumentModel):
    document = models.FileField(upload_to = 'infrastructure/documents/infrastructure_description/', blank=True, verbose_name=_('document'))
    image = models.ImageField(upload_to = 'infrastructure/infrastructure_description/documents/images/', default = 'infrastructure/infrastructure_description/documents/images/none/default.svg', blank=True, verbose_name=_('image'))
    infrastructure_description = models.ForeignKey('registry.InfrastructureDescription', related_name='documents', verbose_name=_('infrastructure description'))


class DataExchangeFormatServiceDocument(DocumentModel):
    document = models.FileField(upload_to = 'infrastructure/data_exchange_formats/documents/services/', blank=True, verbose_name=_('document'))
    image = models.ImageField(upload_to = 'infrastructure/data_exchange_formats/documents/services/images/', default = 'infrastructure/data_exchange_formats/documents/services/images/none/applications/default.svg', blank=True, verbose_name=_('image'))
    data_exchange_format = models.ForeignKey('registry.DataExchangeFormatService', related_name='documents', verbose_name=_('data exchange format'))


class DataExchangeFormatApplicationDocument(DocumentModel):
    document = models.FileField(upload_to = 'infrastructure/documents/data_exchange_formats/applications/', blank=True, verbose_name=_('document'))
    image = models.ImageField(upload_to = 'infrastructure/documents/data_exchange_formats/applications/images/', default = 'infrastructure/documents/data_exchange_formats/applications/images/none/default.svg', blank=True, verbose_name=_('image'))
    data_exchange_format = models.ForeignKey('registry.DataExchangeFormatApplication', related_name='documents', verbose_name=_('data exchange format'))


class TechnicalInterfaceDocument(DocumentModel):
    document = models.FileField(upload_to = 'services/technical_interfaces/documents/', blank=True, verbose_name=_('document'))
    image = models.ImageField(upload_to = 'services/technical_interfaces/documents/images/', default = 'services/technical_interfaces/documents/images/none/default.svg', blank=True, verbose_name=_('image'))
    technical_interface = models.ForeignKey('registry.TechnicalInterface', related_name='documents', verbose_name=_('technical interface'))


class ServiceDocument(DocumentModel):
    document = models.FileField(upload_to = 'services/documents/', blank=True, verbose_name=_('document'))
    image = models.ImageField(upload_to = 'services/documents/images/', default = 'services/documents/images/none/default.svg', blank=True, verbose_name=_('image'))
    service = models.ForeignKey('registry.Service', related_name='documents', verbose_name=_('service'))


class ApplicationDocument(DocumentModel):
    document = models.FileField(upload_to = 'applications/documents/', blank=True, verbose_name=_('document'))
    image = models.ImageField(upload_to = 'applications/documents/images/', default = 'applications/documents/images/none/default.svg', blank=True, verbose_name=_('image'))
    application = models.ForeignKey('registry.Application', related_name='applications', verbose_name=_('application'))


class ParticipantDocument(DocumentModel):
    document = models.FileField(upload_to = 'participants/documents/', blank=True, verbose_name=_('document'))
    image = models.ImageField(upload_to = 'participants/documents/images/', default = 'participants/documents/images/none/default.svg', blank=True, verbose_name=_('image'))
    participant = models.ForeignKey('community.Participant', related_name='documents', verbose_name=_('participant'))

