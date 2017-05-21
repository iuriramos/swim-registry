from django.db import models
from django.contrib.auth.models import User
from swim_registry.models import TimeStampedModel


class Profile(TimeStampedModel):
    NEVER = 'NEVER'
    IMMEDIATE = 'IMMEDIATE'
    DAILY = 'DAILY'
    WEEKLY = 'WEEKLY'

    FREQ_CHOICES = (
        (NEVER, 'Never'),
        (IMMEDIATE, 'Immediate'),
        (DAILY, 'Daily'),
        (WEEKLY,  'Weekly'),
    )

    user = models.OneToOneField(User, related_name='profile')
    organization = models.OneToOneField('community.Participant', related_name='profile', null=True)
    following_organizations = models.ManyToManyField('community.Participant', related_name='followers')
    notification_frequency = models.CharField(max_length=10, choices=FREQ_CHOICES, default=NEVER)
    subscriptions_content_type = models.ManyToManyField('registry.SubscriptionContentType', related_name='profiles')
    subscriptions_region = models.ManyToManyField('registry.RegionCategory', related_name='profiles')
    subscriptions_stakeholder = models.ManyToManyField('registry.StakeholderCategory', related_name='profiles')
    subscriptions_data = models.ManyToManyField('registry.DataCategory', related_name='profiles')
    subscriptions_activity = models.ManyToManyField('registry.ActivityCategory', related_name='profiles')
    subscriptions_flight_phase = models.ManyToManyField('registry.FlightPhaseCategory', related_name='profiles')

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
