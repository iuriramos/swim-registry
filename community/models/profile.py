from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from swim_registry.models import TimeStampedModel


class Profile(TimeStampedModel):
    NEVER = 'NEVER'
    IMMEDIATE = 'IMMEDIATE'
    DAILY = 'DAILY'
    WEEKLY = 'WEEKLY'

    FREQ_CHOICES = (
        (NEVER, _('Never')),
        (IMMEDIATE, _('Immediate')),
        (DAILY,_('Daily')),
        (WEEKLY,  _('Weekly')),
    )

    user = models.OneToOneField(User, related_name='profile', verbose_name=_('user'))
    organization = models.OneToOneField('community.Participant', related_name='profile', null=True, verbose_name=_('organization'))
    following_organizations = models.ManyToManyField('community.Participant', related_name='followers', verbose_name=_('following organizations'))
    notification_frequency = models.CharField(max_length=10, choices=FREQ_CHOICES, default=NEVER, verbose_name=_('notification frequency'))
    subscriptions_content_type = models.ManyToManyField('registry.SubscriptionContentType', related_name='profiles', verbose_name=_('content type subscriptions'))
    subscriptions_region = models.ManyToManyField('registry.RegionCategory', related_name='profiles', verbose_name=_('region subscriptions'))
    subscriptions_stakeholder = models.ManyToManyField('registry.StakeholderCategory', related_name='profiles', verbose_name=_('stakeholder subscriptions'))
    subscriptions_data = models.ManyToManyField('registry.DataCategory', related_name='profiles', verbose_name=_('ATM data subscriptions'))
    subscriptions_activity = models.ManyToManyField('registry.ActivityCategory', related_name='profiles', verbose_name=_('ATM activity subscriptions'))
    subscriptions_flight_phase = models.ManyToManyField('registry.FlightPhaseCategory', related_name='profiles', verbose_name=_('flight phases subscriptions'))

    class Meta:
        verbose_name=_('profile')

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def email(self):
        return self.user.email

    def set_password(self, password):
        self.user.set_password(password)
        self.user.save()

    def __str__(self):
        return '{self.user.last_name}, {self.user.first_name}'.format(self=self)
