from django.core.mail import send_mail

from .templates.community.confirmation_email import CONFIRMATION_MESSAGE
from swim_registry.settings.base import DEFAULT_FROM_EMAIL


def send_confirmartion_mail(email, password):
    message = CONFIRMATION_MESSAGE.format(email, password)
    send_mail('SWIM Registry Brazil - Confirmation request', message, DEFAULT_FROM_EMAIL, (self.email, ), fail_silently=False)
