from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from .models.profile import Profile
from .models.participant import Participant
from .models.registration_request import RegistrationRequest


class RegistrationRequestForm(forms.ModelForm):
    approved = forms.TypedChoiceField(required=False, coerce=lambda x: x =='True',
                                   choices=((False, 'No'), (True, 'Yes')), label=_('approved'))

    class Meta:
        model = RegistrationRequest
        fields = '__all__'
        widgets = {
            'first_name': widgets.TextInput(attrs={'id': 'first_name_id', 'class': 'form-control', 'autofocus': True}),
            'last_name': widgets.TextInput(attrs={'id': 'last_name_id', 'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'id': 'email_id', 'class': 'form-control'}),
            'organization': widgets.TextInput(attrs={'id': 'organization_id', 'class': 'form-control'}),
            'role': widgets.TextInput(attrs={'id': 'role_id', 'class': 'form-control'}),
            'note': widgets.Textarea(attrs={'id': 'note_id', 'class': 'form-control', 'placeholder': _('Describe how you intend to use the SWIM Registry.')}),
            'approved': widgets.Select(),
         }

    def save(self, commit=True):
        request = super().save(commit=commit)
        approved = self.cleaned_data.get('approved', None)
        if approved:
            request.register()
        return request

    def is_valid(self):
        if not super().is_valid():
            return False
        user_exists = User.objects.filter(username=self.cleaned_data['email']).exists()
        if user_exists:
            self.add_error('email', ValidationError(_('Email already registered'), code='invalid_email'))
            return False
        return True


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255, required=True, label=_('first name'))
    last_name = forms.CharField(max_length=255, required=True, label=_('last name'))
    email = forms.EmailField(max_length=255, required=True, label=_('email'))

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'notification_frequency']
        widgets = {
            'notification_frequency': widgets.Select(attrs={'id': 'notification_frequency_id', 'class': 'form-control'}),
        }


class ParticipantForm(forms.ModelForm):

    class Meta:
        model = Participant
        # exclude = ['displayable']
        exclude = ['displayable', 'contact_points', 'documents']
        widgets = {
            'name': widgets.TextInput(attrs={'id': 'name_id', 'class': 'form-control', 'placeholder': _('Name')}),
            'description': widgets.Textarea(attrs={'id': 'description_id', 'class': 'form-control', 'placeholder': _('Description')}),
            'category': widgets.Select(attrs={'id': 'category_id', 'class': 'form-control'}),
        }

