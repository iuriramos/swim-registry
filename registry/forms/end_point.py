from django import forms
from django.forms import inlineformset_factory
from registry.models.technical_interface import TechnicalInterface
from registry.models.end_point import EndPoint


EndPointFormSet = inlineformset_factory(
    TechnicalInterface, EndPoint,
    widgets = {
        'name': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
        'description': forms.widgets.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        'address': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    }, extra=0, fields='__all__')

