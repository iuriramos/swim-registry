from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models.profile import Profile
from .models.participant import Participant
from .models.registration_request import RegistrationRequest


class RegistrationRequestForm(forms.ModelForm):
    approved = forms.TypedChoiceField(required=False, coerce=lambda x: x =='True',
                                   choices=((False, 'No'), (True, 'Yes')))

    class Meta:
        model = RegistrationRequest
        fields = '__all__'
        widgets = {
            'first_name': widgets.TextInput(attrs={'id': 'first_name_id', 'class': 'form-control', 'autofocus': True, 'placeholder': 'First name'}),
            'last_name': widgets.TextInput(attrs={'id': 'last_name_id', 'class': 'form-control', 'placeholder': 'Last name'}),
            'email': widgets.TextInput(attrs={'id': 'email_id', 'class': 'form-control', 'placeholder': 'E-mail'}),
            'organization': widgets.TextInput(attrs={'id': 'organization_id', 'class': 'form-control', 'placeholder': 'Organization'}),
            'role': widgets.TextInput(attrs={'id': 'role_id', 'class': 'form-control', 'placeholder': 'Role'}),
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
            self.add_error('email', ValidationError('email already registered', code='invalid_email'))
            return False
        return True


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'notification_frequency']
        widgets = {
            'notification_frequency': widgets.Select(attrs={'id': 'notification_frequency_id', 'class': 'form-control'}),
        }


# class OrganizationForm(forms.ModelForm):

#     class Meta:
#         model = Participant
#         fields = ['name', 'email', 'description']
#         widgets = {
#             'name': widgets.TextInput(attrs={'id': 'name_id', 'class': 'form-control', 'autofocus': True, 'placeholder': 'Organization name', 'readonly': 'readonly'}),
#             'email': widgets.TextInput(attrs={'id': 'email_id', 'class': 'form-control', 'placeholder': 'E-mail'}),
#             'description': widgets.Textarea(attrs={'id': 'description_id', 'class': 'form-control', 'placeholder': 'Description'}),
#          }



