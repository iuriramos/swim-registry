from django import forms
from django.forms import inlineformset_factory
from registry.models.technical_interface import TechnicalInterface
from registry.models.data_exchange_format import DataExchangeFormatService


DataExchangeFormatServiceFormSet = inlineformset_factory(
    TechnicalInterface, DataExchangeFormatService,
    widgets = {
        'name': forms.widgets.TextInput(attrs={'id': 'id_data_exchange_format_services-name', 'class': 'form-control', 'placeholder': 'Data exchange format name'}),
        'description': forms.widgets.Textarea(attrs={'id': 'id_data_exchange_format_services-description', 'class': 'form-control', 'placeholder': 'Data exchange format description'}),
        'version': forms.widgets.TextInput(attrs={'id': 'id_data_exchange_format_services-version', 'class': 'form-control', 'placeholder': 'Data exchange format version'}),
        'infrastructure_reference_documents': forms.widgets.SelectMultiple(attrs={'id': 'id_data_exchange_format_services-infrastructure_reference_documents_id', 'class': 'form-control'}),
    }, extra=0, fields='__all__')

#     image = models.ImageField(upload_to = 'data/data_exchange_formats/images/', default = 'data/data_exchange_formats/images/none/default.jpg')

# # infrastructure_documents = models.ManyToManyField(InfrastructureDocument, related_name='data_exchange_formats')
