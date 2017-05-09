from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import RegistrationRequest


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
        approved = self.cleaned_data.get('approved', None)
        if approved:
            request.register()
        return super().save(commit=commit)

    def is_valid(self):
        if not super().is_valid():
            return False
        user_exists = User.objects.filter(username=self.cleaned_data['email']).exists()
        if user_exists:
            self.add_error('email', ValidationError('email already registered', code='invalid_email'))
            return False
        return True

