from django.db import models
from django.contrib.auth.models import User

from swim_registry.models import TimeStampedModel
from registry.models.subscription_content_type import SubscriptionContentType
from registry.models.region_category import RegionCategory
from registry.models.data_category import DataCategory
from registry.models.activity_category import ActivityCategory
from registry.models.flight_phase_category import FlightPhaseCategory
from registry.models.stakeholder_category import StakeholderCategory

from .participant import Participant


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
    organization = models.OneToOneField(Participant, related_name='profile', null=True)
    following_organizations = models.ManyToManyField(Participant, related_name='followers')
    notification_frequency = models.CharField(max_length=10, choices=FREQ_CHOICES, default=NEVER)
    subscriptions_content_type = models.ManyToManyField(SubscriptionContentType, related_name='profiles')
    subscriptions_region = models.ManyToManyField(RegionCategory, related_name='profiles')
    subscriptions_stakeholder = models.ManyToManyField(StakeholderCategory, related_name='profiles')
    subscriptions_data = models.ManyToManyField(DataCategory, related_name='profiles')
    subscriptions_activity = models.ManyToManyField(ActivityCategory, related_name='profiles')
    subscriptions_flight_phase = models.ManyToManyField(FlightPhaseCategory, related_name='profiles')

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
