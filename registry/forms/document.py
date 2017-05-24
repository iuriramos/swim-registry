from django import forms
from django.forms import inlineformset_factory
from community.models.participant import Participant
from registry.models.service import Service
from registry.models.technical_interface import TechnicalInterface
from registry.models.infrastructure import InfrastructureDescription
from registry.models.data_exchange_format import DataExchangeFormatService
from registry.models.document import ParticipantDocument, InfrastructureDescriptionDocument, ServiceDocument, TechnicalInterfaceDocument, DataExchangeFormatServiceDocument


ParticipantDocumentFormSet = inlineformset_factory(
    Participant, ParticipantDocument,
    widgets = {
        'name': forms.widgets.TextInput(attrs={'id': 'id_participant_document-name', 'class': 'form-control', 'placeholder': 'Name'}),
        'description': forms.widgets.Textarea(attrs={'id': 'id_participant_document-description', 'class': 'form-control', 'placeholder': 'Description'}),
        'version': forms.widgets.TextInput(attrs={'id': 'id_participant_document-version', 'class': 'form-control', 'placeholder': 'Version'}),
    }, extra=1, exclude=('document', )) # TODO: fields='__all__'


InfrastructureDescriptionDocumentFormSet = inlineformset_factory(
    InfrastructureDescription, InfrastructureDescriptionDocument,
    widgets = {
        'name': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
        'description': forms.widgets.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        'version': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Version'}),
    }, extra=1, fields='__all__')


DataExchangeFormatServiceDocumentFormSet = inlineformset_factory(
    DataExchangeFormatService,  DataExchangeFormatServiceDocument,
    widgets = {
        'name': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
        'description': forms.widgets.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        'version': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Version'}),
    }, extra=1, fields='__all__')


ServiceDocumentFormSet = inlineformset_factory(
    Service, ServiceDocument,
    widgets = {
        'name': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
        'description': forms.widgets.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        'version': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Version'}),
        'external_link': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'External Link'}),
        },extra=1, fields='__all__')

TechnicalInterfaceDocumentFormSet = inlineformset_factory(
    TechnicalInterface, TechnicalInterfaceDocument,
    widgets = {
        'name': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
        'description': forms.widgets.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        'version': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Version'}),
        'external_link': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'External Link'}),
        }, extra=1, fields='__all__')
