from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from registry.models.service import Service
from registry.models.version_category import VersionCategory
from registry.models.implementation import ImplementationMaturityCategory, ImplementationStatusCategory
from registry.models.registration_status_category import RegistrationStatusCategory
from registry.models.data_category import DataCategory
from registry.models.activity_category import ActivityCategory
from registry.models.stakeholder_category import StakeholderCategory
from registry.models.flight_phase_category import FlightPhaseCategory
from registry.models.region_category import RegionCategory


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        exclude = ['organization', 'reviewed', 'workflow', 'technical_interface']
        widgets = {
            'name': forms.widgets.TextInput(attrs={'id': 'name_id', 'class': 'form-control', 'placeholder': _('Name')}),
            'description': forms.widgets.Textarea(attrs={'id': 'description_id', 'class': 'form-control', 'placeholder': _('Description')}),
            'version': forms.widgets.TextInput(attrs={'id': 'version_id', 'class': 'form-control', 'placeholder': _('Version')}),
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


class ServiceSearchForm(forms.Form):
    name = forms.CharField(label=_('Service Name'), max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label=_('Description'), max_length=255, required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    version_category = forms.MultipleChoiceField(label=_('Version Category'), required=False, choices=VersionCategory.CHOICES, widget=forms.widgets.SelectMultiple(attrs={'class': 'form-control'}))
    implementation_status = forms.MultipleChoiceField(label=_('Implementation Status'), required=False, choices=ImplementationStatusCategory.CHOICES, widget=forms.widgets.SelectMultiple(attrs={'class': 'form-control'}))
    implementation_maturity = forms.MultipleChoiceField(label=_('Implementation Maturity'), required=False, choices=ImplementationMaturityCategory.CHOICES, widget=forms.widgets.SelectMultiple(attrs={'class': 'form-control'}))
    registration_status = forms.MultipleChoiceField(label=_('Registration Status'), required=False, choices=RegistrationStatusCategory.CHOICES, widget=forms.widgets.SelectMultiple(attrs={'class': 'form-control'}))
    data_categories = forms.MultipleChoiceField(label=_('Data Category'), required=False, choices=DataCategory.CHOICES, widget=forms.widgets.SelectMultiple(attrs={'class': 'form-control'}))
    activity_categories = forms.MultipleChoiceField(label=_('Activity Category'), required=False, choices=ActivityCategory.CHOICES, widget=forms.widgets.SelectMultiple(attrs={'class': 'form-control'}))
    stakeholders = forms.MultipleChoiceField(label=_('Stakeholder'), required=False, choices=StakeholderCategory.CHOICES, widget=forms.widgets.SelectMultiple(attrs={'class': 'form-control'}))
    regions = forms.MultipleChoiceField(label=_('Region'), required=False, choices=RegionCategory.CHOICES, widget=forms.widgets.SelectMultiple(attrs={'class': 'form-control'}))
    flight_phases = forms.MultipleChoiceField(label=_('Flight Phase'), required=False, choices=FlightPhaseCategory.CHOICES, widget=forms.widgets.SelectMultiple(attrs={'class': 'form-control'}))

