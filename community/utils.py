from django.core.mail import send_mail

from .templates.community.confirmation_email import TEMPLATE_CONFIRMATION_MSG
from swim_registry.settings.base import DEFAULT_FROM_EMAIL


def send_confirmartion_mail(email, password):
    message = TEMPLATE_CONFIRMATION_MSG.format(email=email, password=password)
    send_mail('SWIM Registry Brazil - Confirmation request', message, DEFAULT_FROM_EMAIL, (email, ), fail_silently=False)
