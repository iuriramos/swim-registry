from django import forms
from django.forms import inlineformset_factory
from community.models.participant import Participant
from registry.models.service import Service
from registry.models.contact_point import ContactPointParticipant
from registry.models.contact_point import ContactPointService


ContactPointParticipantFormSet = inlineformset_factory(
    Participant, ContactPointParticipant,
    widgets = {
        'name': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
        'description': forms.widgets.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        'email': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        'telephone': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telephone'}),
    }, extra=1, fields='__all__')


ContactPointServiceFormSet = inlineformset_factory(
    Service, ContactPointService,
    widgets = {
        'name': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
        'description': forms.widgets.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        'email': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        'telephone': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telephone'}),
    }, extra=1, fields='__all__')

