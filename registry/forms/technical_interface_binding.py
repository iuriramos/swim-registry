from django import forms
from django.forms import inlineformset_factory
from registry.models.technical_interface_binding import TechnicalInterfaceBindingDescription
from registry.models.infrastructure import InfrastructureDescription


TechnicalInterfaceBindingDescriptionFormSet = inlineformset_factory(
    InfrastructureDescription, TechnicalInterfaceBindingDescription,
    widgets = {
        'name': forms.widgets.TextInput(attrs={'id': 'id_contact_points-name', 'class': 'form-control', 'placeholder': 'Name'}),
        'description': forms.widgets.Textarea(attrs={'id': 'id_contact_points-description', 'class': 'form-control', 'placeholder': 'Description'}),
    }, extra=1, fields='__all__')

# image = models.ImageField(upload_to = 'infrastructure/technical_interface_bindings/images/', default = 'infrastructure/technical_interface_bindings/images/none/default.jpg')
