from django.db import models

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
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    version = models.CharField(max_length=50, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

