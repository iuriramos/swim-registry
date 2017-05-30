from django.db import models
from django.utils.translation import ugettext_lazy as _


class RegistrationStatusCategory(models.Model):
    DRAFT = 'DRAFT'
    VALIDATION = 'VALIDATION'
    REGISTERED = 'REGISTERED'

    CHOICES = (
        (DRAFT, _('Draft')),
        (VALIDATION, _('Validation')),
        (REGISTERED, _('Registered')),
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True)

    class Meta:
        verbose_name = _('registration status category')
        verbose_name_plural = _('registration status categories')

    def __str__(self):
        return self.name
