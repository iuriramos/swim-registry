from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from swim_registry.models import TimeStampedModel
from .profile import Profile
from community.utils import send_confirmartion_mail


class RegistrationRequest(TimeStampedModel):
    first_name = models.CharField(max_length=255, verbose_name=_('first name'))
    last_name = models.CharField(max_length=255, verbose_name=_('last name'))
    email = models.EmailField(verbose_name=_('email'))
    organization = models.CharField(max_length=255, verbose_name=_('organization'))
    role = models.CharField(max_length=255, verbose_name=_('institutional role'))
    note = models.TextField(verbose_name=_('note'))

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
        send_confirmartion_mail(profile.full_name, self.email, password)
        
    class Meta:
        verbose_name=_('registration request')

    def __str__(self):
        return '{self.last_name}, {self.first_name}'.format(self=self)
