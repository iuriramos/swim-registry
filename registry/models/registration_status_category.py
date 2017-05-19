from django.db import models


class RegistrationStatusCategory(models.Model):
    DRAFT = 'DRAFT'
    VALIDATION = 'VALIDATION'
    REGISTERED = 'REGISTERED'

    CHOICES = (
        (DRAFT, 'Draft'),
        (VALIDATION, 'Validation'),
        (REGISTERED, 'Registered'),
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True)

    class Meta:
        verbose_name = 'registration status category'
        verbose_name_plural = 'registration status categories'

    def __str__(self):
        return self.name
