from django import forms
from django.forms import inlineformset_factory
from community.models.participant import Participant
from registry.models.service import Service
from registry.models.infrastructure import InfrastructureDescription
from registry.models.document import ParticipantDocument, InfrastructureDescriptionDocument, ServiceDocument


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
        'name': forms.widgets.TextInput(attrs={'id': 'id_infrastructure_description_document-name', 'class': 'form-control', 'placeholder': 'Name'}),
        'description': forms.widgets.Textarea(attrs={'id': 'id_infrastructure_description_document-description', 'class': 'form-control', 'placeholder': 'Description'}),
        'version': forms.widgets.TextInput(attrs={'id': 'id_infrastructure_description_document-version', 'class': 'form-control', 'placeholder': 'Version'}),
    }, extra=1, exclude=('document', )) # TODO: fields='__all__'


ServiceDocumentFormSet = inlineformset_factory(
    Service, ServiceDocument,
    widgets = {
        'name': forms.widgets.TextInput(attrs={'id': 'id_service_document-name', 'class': 'form-control', 'placeholder': 'Name'}),
        'description': forms.widgets.Textarea(attrs={'id': 'id_service_document-description', 'class': 'form-control', 'placeholder': 'Description'}),
        'version': forms.widgets.TextInput(attrs={'id': 'id_service_document-version', 'class': 'form-control', 'placeholder': 'Version'}),
    }, extra=1, exclude=('document', )) # TODO: fields='__all__'

