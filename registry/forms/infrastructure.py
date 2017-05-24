from django import forms
from django.core.exceptions import ValidationError
from registry.models.infrastructure import InfrastructureDescription


class InfrastructureDescriptionForm(forms.ModelForm):

    class Meta:
        model = InfrastructureDescription
        fields = '__all__'
        widgets = {
            'description': forms.widgets.Textarea(attrs={'id': 'infrastructure_description__description_id', 'class': 'form-control', 'placeholder': 'Infrastructure Description'}),
            'version': forms.widgets.TextInput(attrs={'id': 'infrastructure_description__version_id', 'class': 'form-control', 'placeholder': 'Technical Interface Version'}),
            'infrastructure_reference_documents': forms.widgets.SelectMultiple(attrs={'id': 'infrastructure_description__infrastructure_reference_documents_id', 'class': 'form-control'}),
        }

    # image = models.ImageField(upload_to = 'infrastructure/profiles/images/', default = 'infrastructure/profiles/images/none/default.jpg')
