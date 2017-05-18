from django.db import models


class VersionCategory(models.Model):
    CURRENT_AND_SUPPORTED = 'CURRENT AND SUPPORTED'
    NON_SUPPORTED = 'NON SUPPORTED'
    OBSOLETE_BUT_SUPPORTED = 'OBSOLETE BUT SUPPORTED'
    UPCOMING_NOT_SUPPORTED = 'UPCOMING NOT SUPPORTED'

    CHOICES = (
        CURRENT_AND_SUPPORTED, 'Current and Supported',
        NON_SUPPORTED, 'Non Supported',
        OBSOLETE_BUT_SUPPORTED, 'Obsolete but Supported',
        UPCOMING_NOT_SUPPORTED, 'Upcoming not Supported',
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True)

    class Meta:
        verbose_name = 'version category'
        verbose_name_plural = 'version categories'

    def __str__(self):
        return self.name
