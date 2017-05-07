from django.contrib import admin
from .models import RegistrationRequest, UserAccount

from .forms import RegistrationRequestForm

# change admin site header
admin.site.site_header = 'SWIM administration'

# admin.site.register(RegistrationRequest)
admin.site.register(UserAccount)

class RegistrationRequestAdmin(admin.ModelAdmin):
    form = RegistrationRequestForm

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'organization', 'role', ),
        }),
        (None, {
            'fields': ('approved', ),
        }),
    )

admin.site.register(RegistrationRequest, RegistrationRequestAdmin)
