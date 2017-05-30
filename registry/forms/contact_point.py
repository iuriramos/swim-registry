from django import forms
from django.forms import inlineformset_factory
from django.utils.translation import ugettext_lazy as _
from community.models.participant import Participant
from registry.models.service import Service
from registry.models.contact_point import ContactPointParticipant
from registry.models.contact_point import ContactPointService


ContactPointParticipantFormSet = inlineformset_factory(
    Participant, ContactPointParticipant,
    widgets = {
        'name': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': _('Name')}),
        'description': forms.widgets.Textarea(attrs={'class': 'form-control', 'placeholder': _('Description')}),
        'email': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': _('Email')}),
        'telephone': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': _('Telephone')}),
    }, extra=0, fields='__all__')


ContactPointServiceFormSet = inlineformset_factory(
    Service, ContactPointService,
    widgets = {
        'name': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': _('Name')}),
        'description': forms.widgets.Textarea(attrs={'class': 'form-control', 'placeholder': _('Description')}),
        'email': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': _('Email')}),
        'telephone': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': _('Telephone')}),
    }, extra=0, fields='__all__')

