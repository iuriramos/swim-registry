from django.contrib import admin

from .models import RegistrationRequest, Profile, Participant
from .forms import RegistrationRequestForm


class RegistrationRequestAdmin(admin.ModelAdmin):
    form = RegistrationRequestForm
    fields = ('first_name', 'last_name', 'email', 'organization', 'role', 'approved', )


admin.site.register(RegistrationRequest, RegistrationRequestAdmin)
admin.site.register(Participant)
admin.site.register(Profile)
