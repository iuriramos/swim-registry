from django.db import models
from django.contrib.auth.models import User

from swim_registry.models import TimeStampedModel
from registry.models import SubscriptionContentType, RegionCategory, FlightCategory, FlightPhaseCategory, StakeholderCategory

from .utils import send_confirmartion_mail


class RegistrationRequest(TimeStampedModel):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False)
    organization = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    def register(self):
        password = User.objects.make_random_password()
        user = User.objects.create_user(
                        username=self.email,
                        email=self.email,
                        password=password,
                        first_name=self.first_name,
                        last_name=self.last_name
                    )
        profile = Profile(
                            user=user,
                            # TODO
                        )
        profile.save()
        send_confirmartion_mail(self.email, password)
        self.delete()

    def __str__(self):
        return '{self.last_name}, {self.first_name}'.format(self=self)


class Participant(TimeStampedModel):
    name = models.CharField(max_length=255, null=False)
    email =  models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name


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
    organization = models.ForeignKey(Participant, related_name='profiles', null=True)
    following_organizations = models.ManyToManyField(Participant, related_name='followers')
    notification_frequency = models.CharField(max_length=10, choices=FREQ_CHOICES, default=NEVER)
    subscriptions_content_type = models.ManyToManyField(SubscriptionContentType, related_name='profiles')
    subscriptions_region = models.ManyToManyField(RegionCategory, related_name='profiles')
    subscriptions_stakeholder = models.ManyToManyField(StakeholderCategory, related_name='profiles')
    subscriptions_flight = models.ManyToManyField(FlightCategory, related_name='profiles')
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

