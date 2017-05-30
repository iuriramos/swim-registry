from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from swim_registry.settings.base import DEFAULT_FROM_EMAIL
from .consts import TEMPLATE_CONFIRMATION_MSG


def send_confirmartion_mail(email, password):
    message = _(TEMPLATE_CONFIRMATION_MSG).format(email=email, password=password)
    send_mail(_('SWIM Registry Brazil - Confirmation request'), message, DEFAULT_FROM_EMAIL, (email, ), fail_silently=False)
