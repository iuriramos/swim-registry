from django import forms
from django.forms import inlineformset_factory
from community.models.participant import Participant
from registry.models.contact_point import ContactPointParticipant


ContactPointParticipantFormSet = inlineformset_factory(
    Participant, ContactPointParticipant,
    widgets = {
        'name': forms.widgets.TextInput(attrs={'id': 'id_contact_points-name', 'class': 'form-control', 'placeholder': 'Name'}),
        'description': forms.widgets.Textarea(attrs={'id': 'id_contact_points-description', 'class': 'form-control', 'placeholder': 'Description'}),
        'email': forms.widgets.TextInput(attrs={'id': 'id_contact_points-email', 'class': 'form-control', 'placeholder': 'Email'}),
        'telephone': forms.widgets.TextInput(attrs={'id': 'id_contact_points-telephone', 'class': 'form-control', 'placeholder': 'Telephone'}),
    }, extra=1, fields='__all__')
