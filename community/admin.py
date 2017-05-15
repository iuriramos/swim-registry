from django.contrib import admin

from .models.profile import Profile
from .models.participant import Participant
from .models.registration_request import RegistrationRequest
from .forms import RegistrationRequestForm


class RegistrationRequestAdmin(admin.ModelAdmin):
    form = RegistrationRequestForm
    fields = ('first_name', 'last_name', 'email', 'organization', 'role', 'approved', )


admin.site.register(RegistrationRequest, RegistrationRequestAdmin)
admin.site.register(Participant)
admin.site.register(Profile)
