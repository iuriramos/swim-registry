from django import forms
from django.core.exceptions import ValidationError
from registry.models.service import Service


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        exclude = ['organization', 'reviewed', 'workflow']
        widgets = {
            'name': forms.widgets.TextInput(attrs={'id': 'name_id', 'class': 'form-control', 'placeholder': 'Name'}),
            'version': forms.widgets.TextInput(attrs={'id': 'version_id', 'class': 'form-control', 'placeholder': 'Version'}),
            'version_category': forms.widgets.Select(attrs={'id': 'version_category_id', 'class': 'form-control'}),
            'implementation_status': forms.widgets.Select(attrs={'id': 'implementation_status_id', 'class': 'form-control'}),
            'implementation_maturity': forms.widgets.Select(attrs={'id': 'implementation_maturity_id', 'class': 'form-control'}),
            'registration_status': forms.widgets.Select(attrs={'id': 'registration_status_id', 'class': 'form-control'}),
            'data_categories': forms.widgets.SelectMultiple(attrs={'id': 'data_categories_id', 'class': 'form-control'}),
            'activity_categories': forms.widgets.SelectMultiple(attrs={'id': 'activity_categories_id', 'class': 'form-control'}),
            'stakeholders': forms.widgets.SelectMultiple(attrs={'id': 'stakeholders_id', 'class': 'form-control'}),
            'regions': forms.widgets.SelectMultiple(attrs={'id': 'regions_id', 'class': 'form-control'}),
            'flight_phases': forms.widgets.SelectMultiple(attrs={'id': 'flight_phases_id', 'class': 'form-control'}),
        }

    # = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
    # organization = models.ForeignKey('community.Participant', related_name='services')
    # image = models.ImageField(upload_to = 'services/images/profiles/', default = 'services/images/profiles/none/default.jpg')

    # technical_interface = models.OneToOneField('registry.TechnicalInterface', related_name='service')
    # # documents = models.ManyToManyField(ServiceDocument, related_name='services')
    # # contact_points = models.ManyToManyField(ContactPoint, related_name='services')
    # # # events = models.ManyToManyField(Event, related_name='services')
    # # #  quality_service_conditions = models.OneToOneField(TechnicalInterface, related_name='services')

    # reviewed = models.BooleanField(default=False)
    # workflow = models.OneToOneField('registry.Workflow', related_name='service')

