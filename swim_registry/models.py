from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides
    self-updating fields ``created`` and ``modified``
    """
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    modified = models.DateTimeField(auto_now=True, verbose_name=_('modified'))

    class Meta:
        abstract = True


class DocumentModel(models.Model):
    """
    An abstract base class model that provides
    name, description and self-updating fields
    ``created`` and ``modified`` for document models.
    """
    name = models.CharField(max_length=255, blank=False, verbose_name=_('name'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    version = models.CharField(max_length=50, blank=True, verbose_name=_('version'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    modified = models.DateTimeField(auto_now=True, verbose_name=_('modified'))
    external_link = models.URLField(blank=True, verbose_name=_('external link'))

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

