from django.db import models
from django.contrib.auth.models import User
from swim_registry.models import TimeStampedModel


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
        # self.delete()

    def __str__(self):
        return '{self.last_name}, {self.first_name}'.format(self=self)
