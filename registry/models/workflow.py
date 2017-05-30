from django.utils.translation import ugettext_lazy as _
from django.db import models
from swim_registry.models import TimeStampedModel


class Workflow(TimeStampedModel):
    author = models.ForeignKey('community.Profile', related_name='workflows')
    description = models.TextField(blank=True)
    current_state = models.ForeignKey('registry.RegistrationStatusCategory', related_name='workflows_from')
    next_state = models.ForeignKey('registry.RegistrationStatusCategory', related_name='workflows_to')
    previous_node = models.ForeignKey('self')

    def __str__(self):
        return _('From {from_} to {to} by {author}').format(from_=self.current_state, to=self.next_state, author=self.author)
