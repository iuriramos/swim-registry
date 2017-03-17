from django.contrib import admin
from registry.models import RegistrationRequest, UserAccount

from registry.forms import RegistrationRequestForm

# Register your models here.
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
