from django import forms

class ContactPointForm(forms.ModelForm):

    class Meta:
        model = Participant
        fields = '__all__'
        widgets = {
            'name': widgets.TextInput(attrs={'id': 'name_id', 'class': 'form-control', 'placeholder': 'Name'}),
            'description': widgets.Textarea(attrs={'id': 'description_id', 'class': 'form-control', 'placeholder': 'Description'}),
            'email': widgets.TextInput(attrs={'id': 'email_id', 'class': 'form-control', 'placeholder': 'Email'}),
            'telephone': widgets.TextInput(attrs={'id': 'telephone_id', 'class': 'form-control', 'placeholder': 'Telephone'}),
        }
