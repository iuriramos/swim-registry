from django.db import models
from django.utils.translation import ugettext_lazy as _


def make_choices(choices):
    """
    Returns tuples of localized choices based on the dict choices parameter.
    Uses lazy translation for choices names.
    """
    return tuple([(k, _(v)) for k, v in choices.items()])


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides
    self-updating fields ``created`` and ``modified``
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DocumentModel(models.Model):
    """
    An abstract base class model that provides
    name, description and self-updating fields
    ``created`` and ``modified`` for document models.
    """
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    version = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    external_link = models.URLField(blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

