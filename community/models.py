from django.db import models
from django.contrib.auth.models import User

from swim_registry.models import TimeStampedModel
from registry.models import SubscriptionContentType, RegionCategory, DataCategory, FlightPhaseCategory, StakeholderCategory, ActivityCategory

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
        # send_confirmartion_mail(self.email, password)
        # self.delete()

    def __str__(self):
        return '{self.last_name}, {self.first_name}'.format(self=self)


class Participant(TimeStampedModel):
    AIRSPACE_COMPANY = 'AIRSPACE COMPANY'
    RESEARCH_ORGANIZATION = 'RESEARCH ORGANIZATION'
    AIRPORT = 'AIRPORT'
    AERODROME = 'AERODROME'
    RESEARCH_INSTITUTION = 'RESEARCH INSTITUTION'
    PUBLIC_AGENCY = 'PUBLIC AGENCY'
    OTHER = 'OTHER'

    PARTICIPANT_CHOICES = (
        (AIRSPACE_COMPANY, 'Airspace company'),
        (RESEARCH_ORGANIZATION, 'Research Organization'),
        (AIRPORT, 'Airport'),
        (AERODROME, 'Aerodrome'),
        (RESEARCH_INSTITUTION,  'Research Institution'),
        (PUBLIC_AGENCY,  'Public Agency'),
        (OTHER,  'Other'),
    )

    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    category = models.CharField(max_length=255, choices=PARTICIPANT_CHOICES, null=False)
    picture = models.ImageField(upload_to = 'participants/', default = 'participants/None/default.jpg')
    # services = models.ManyToManyField(Service, related_name='participants')
    # applications = models.ManyToManyField(Application, related_name='participants')
    # documentations = models.ManyToManyField(ParticipantDocumentation, related_name='participants')
    # contact_points = models.ManyToManyField(ContactPoint, related_name='participants')

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
    # organizations = models.ManyToManyField(Participant, related_name='profiles')
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


# class RequestOrganization(TimeStampedModel):
#     name = models.CharField(max_length=255, null=False)
#     email = models.EmailField(null=False)
#     role = models.CharField(max_length=255)
#     description = models.TextField()

#     def register(self):
#         password = User.objects.make_random_password()
#         user = User.objects.create_user(
#                         username=self.email,
#                         email=self.email,
#                         password=password,
#                         first_name=self.first_name,
#                         last_name=self.last_name
#                     )
#         profile = Profile(
#                             user=user,
#                             # TODO
#                         )
#         profile.save()
#         send_confirmartion_mail(self.email, password)
#         self.delete()

#     def __str__(self):
#         return '{self.last_name}, {self.first_name}'.format(self=self)

