from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RegistrationRequest(models.Model):

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
        account = UserAccount(
                            user=user,
                            organization=self.organization,
                            role=self.role
                        )
        # TODO: delete registration request
        account.save()
        #RegistrationRequest.objects.get(pk=self.pk).delete()

    def __str__(self):
        return '{0.first_name} {0.last_name}, {0.role}, {0.organization}'.format(self)

class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='user_account')
    organization = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    @property
    def first_name(self):
        return self.user.first_name

    def delete(self, *args, **kwargs):
        self.user.delete()
        return super(self.__class__, self).delete(*args, **kwargs)

    def set_password(self, password):
        self.user.set_password(password)
        self.user.save()

    def __str__(self):
        return '{0.user.username}, {0.role}, {0.organization}'.format(self)

