from django import forms
from django.contrib.auth.models import User

from .models import RegistrationRequest

class RegisterAccountForm(forms.Form):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    # password = forms.CharField(required=True)
    organization = forms.CharField(required=False)
    role = forms.CharField(required=False)

    def is_valid(self):
        if not super(RegisterAccountForm, self).is_valid():
            self.append_error('Please, check out your information')
            return False

        if User.objects.filter(email=self.data['email']).exists():
            self.append_error('User already registered')
            return False

        return True

    def append_error(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)

class RegistrationRequestForm(forms.ModelForm):
    approved = forms.BooleanField()

    def save(self, commit=True):
        approved = self.cleaned_data.get('approved', None)
        if approved:
            print ("approved")
            print (self)
        return super(RegistrationRequestForm, self).save(commit=commit)

    class Meta:
        model = RegistrationRequest
        fields = '__all__'
