from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from registry.models.review_request import ReviewRequestService


class ReviewRequestServiceForm(forms.ModelForm):

    class Meta:
        model = ReviewRequestService
        exclude = ['service', 'workflow']
        # fields='__all__'
        widgets = {
            'description': forms.widgets.Textarea(attrs={'class': 'form-control', 'placeholder': _('Describe the changes made to the service.\nInformation will be public in the service workflow.')}),
        }

class ReviewRequestServiceAdminForm(forms.ModelForm):

    class Meta:
        model = ReviewRequestService
        fields='__all__'

    def save(self, commit=True):
        request = super().save(commit=commit)
        approved = self.cleaned_data.get('approved', None)
        if approved:
            request.approve()
        else:
            request.disapprove()
        return request
