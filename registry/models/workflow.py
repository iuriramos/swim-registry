from django.utils.translation import ugettext_lazy as _
from django.db import models
from swim_registry.models import TimeStampedModel


class Workflow(TimeStampedModel):
    author = models.ForeignKey('community.Profile', related_name='workflows', verbose_name=_('author'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    old_state = models.ForeignKey('registry.RegistrationStatusCategory', related_name='workflows_from', null=True, verbose_name=_('old state'))
    new_state = models.ForeignKey('registry.RegistrationStatusCategory', related_name='workflows_to', verbose_name=_('new state'))
    previous_node = models.ForeignKey('self', verbose_name=_('previous node'))
    approved = models.BooleanField(default=False, verbose_name=_('approved'))

    class Meta:
        verbose_name = _('workflow')

    def __str__(self):
        return _('From {old_state} to {new_state} by {author}').format(old_state=self.old_state, new_state=self.new_state, author=self.author)
