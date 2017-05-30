from django.db import models
from django.utils.translation import ugettext_lazy as _


class SubscriptionContentType(models.Model):
    AIRM_MODEL = 'AIRM MODEL'
    COMPLIANCE_REFERENCE_DOCUMENT = 'COMPLIANCE REFERENCE DOCUMENT'
    CONTACT_POINT = 'CONTACT POINT'
    ORGANISATION_DOCUMENT = 'ORGANISATION DOCUMENT'
    GENERAL_DOCUMENT = 'GENERAL DOCUMENT'
    INFORMATION_REFERENCE_DOCUMENT = 'INFORMATION REFERENCE DOCUMENT'
    INFRASTRUCTURE_PROFILE = 'INFRASTRUCTURE PROFILE'
    REFERENCE_DOCUMENT = 'REFERENCE DOCUMENT'
    INFRASTRUCTURE_STANDARD = 'INFRASTRUCTURE STANDARD'
    INTERFACE = 'INTERFACE'
    ORGANISATION = 'ORGANISATION'
    PROPRIETARY_DATA_EXCHANGE_FORMAT = 'PROPRIETARY DATA EXCHANGE FORMAT'
    SERVICE_IMPLEMENTATION = 'SERVICE IMPLEMENTATION'
    SERVICE_COMPLIANCE_CLAIM = 'SERVICE COMPLIANCE CLAIM'
    SERVICE_DEFINITION = 'SERVICE DEFINITION'
    SERVICE_DEFINITION_PROGRESS = 'SERVICE DEFINITION PROGRESS'
    SERVICE_DOCUMENT = 'SERVICE DOCUMENT'
    SERVICE_END_POINT = 'SERVICE END POINT'
    SERVICE_LOGICAL_MODEL = 'SERVICE LOGICAL MODEL'
    SERVICE_REFERENCE_DOCUMENT = 'SERVICE REFERENCE DOCUMENT'
    DATA_STANDARD = 'DATA STANDARD'

    CHOICES = (
        (AIRM_MODEL,  _('AIRM Model')),
        (COMPLIANCE_REFERENCE_DOCUMENT,  _('Compliance Reference Document')),
        (CONTACT_POINT,  _('Contact Point')),
        (ORGANISATION_DOCUMENT, _('Organisation Document')),
        (GENERAL_DOCUMENT,  _('General Document')),
        (INFORMATION_REFERENCE_DOCUMENT, _('Information Reference Document')),
        (INFRASTRUCTURE_PROFILE,  _('Infrastructure Profile')),
        (REFERENCE_DOCUMENT,  _('Reference Document')),
        (INFRASTRUCTURE_STANDARD,  _('Infrastructure Standard')),
        (INTERFACE,  _('Interface')),
        (ORGANISATION,  _('Organisation')),
        (PROPRIETARY_DATA_EXCHANGE_FORMAT, _('Proprietary Data Exchange Format')),
        (SERVICE_IMPLEMENTATION,  _('Service Implementation')),
        (SERVICE_COMPLIANCE_CLAIM, _('Service Compliance Claim')),
        (SERVICE_DEFINITION, _('Service Definition')),
        (SERVICE_DEFINITION_PROGRESS, _('Service Definition Progress')),
        (SERVICE_DOCUMENT,_('Service Document')),
        (SERVICE_END_POINT, _('Service End Point')),
        (SERVICE_LOGICAL_MODEL, _('Service Logical Model')),
        (SERVICE_REFERENCE_DOCUMENT, _('Service Reference Document')),
        (DATA_STANDARD, _('Data Standard')),
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True)

    def __str__(self):
        return self.name
