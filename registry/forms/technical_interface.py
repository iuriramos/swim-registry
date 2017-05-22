from django import forms
from django.core.exceptions import ValidationError
from registry.models.technical_interface import TechnicalInterface


class TechnicalInterfaceForm(forms.ModelForm):

    class Meta:
        model = TechnicalInterface
        fields = '__all__'
        widgets = {
            'description': forms.widgets.Textarea(attrs={'id': 'technical_interface__description_id', 'class': 'form-control', 'placeholder': 'Technical Interface Description'}),
            'version': forms.widgets.TextInput(attrs={'id': 'technical_interface__version_id', 'class': 'form-control', 'placeholder': 'Technical Interface Version'}),
            'infrastructure_reference_documents': forms.widgets.SelectMultiple(attrs={'id': 'technical_interface__infrastructure_reference_documents_id', 'class': 'form-control'}),
            'data_standards': forms.widgets.SelectMultiple(attrs={'id': 'technical_interface__data_standards_id', 'class': 'form-control'}),
            'infrastructure_profile': forms.widgets.Select(attrs={'id': 'technical_interface__infrastructure_profile_id', 'class': 'form-control'}),
        }

    # image = models.ImageField(upload_to = 'services/technical_interfaces/images/', default = 'services/technical_interfaces/images/none/default.jpg')

