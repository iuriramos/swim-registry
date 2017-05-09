
from django.db import models


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
        (AIRM_MODEL,  'AIRM Model'),
        (COMPLIANCE_REFERENCE_DOCUMENT,  'Compliance Reference Document'),
        (CONTACT_POINT,  'Contact Point'),
        (ORGANISATION_DOCUMENT,  'Organisation Document'),
        (GENERAL_DOCUMENT,  'General Document'),
        (INFORMATION_REFERENCE_DOCUMENT,  'Information Reference Document'),
        (INFRASTRUCTURE_PROFILE,  'Infrastructure Profile'),
        (REFERENCE_DOCUMENT,  'Reference Document'),
        (INFRASTRUCTURE_STANDARD,  'Infrastructure Standard'),
        (INTERFACE,  'Interface'),
        (ORGANISATION,  'Organisation'),
        (PROPRIETARY_DATA_EXCHANGE_FORMAT,  'Proprietary Data Exchange Format'),
        (SERVICE_IMPLEMENTATION,  'Service Implementation'),
        (SERVICE_COMPLIANCE_CLAIM, 'Service Compliance Claim'),
        (SERVICE_DEFINITION, 'Service Definition'),
        (SERVICE_DEFINITION_PROGRESS, 'Service Definition Progress'),
        (SERVICE_DOCUMENT, 'Service Document'),
        (SERVICE_END_POINT, 'Service End Point'),
        (SERVICE_LOGICAL_MODEL, 'Service Logical Model'),
        (SERVICE_REFERENCE_DOCUMENT, 'Service Reference Document'),
        (DATA_STANDARD, 'Data Standard'),
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True)

    def __str__(self):
        return self.name


class FlightCategory(models.Model):
    AERONAUTICAL_INFORMATION = 'AERONAUTICAL INFORMATION'
    METEOROLOGY = 'METEOROLOGY'
    ENVIRONMENT = 'ENVIRONMENT'
    CAPACITY_DEMAND_AND_FLOW = 'CAPACITY DEMAND AND FLOW'
    SURVEILLANCE  = 'SURVEILLANCE'
    OTHER  = 'OTHER'

    CHOICES = (
        (AERONAUTICAL_INFORMATION, 'Aeronautical Information'),
        (METEOROLOGY, 'Meteorology'),
        (ENVIRONMENT, 'Environment'),
        (CAPACITY_DEMAND_AND_FLOW, 'Capacity Demand and Flow'),
        (SURVEILLANCE, 'Surveillance'),
        (OTHER, 'Other'),
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True)

    class Meta:
        verbose_name = 'flight category'
        verbose_name_plural = 'flight categories'

    def __str__(self):
        return self.name


class FlightPhaseCategory(models.Model):
    AIRPORT_RAMP = 'AIRPORT RAMP'
    TAKE_OFF = 'TAKE OFF'
    DEPARTURE = 'DEPARTURE'
    EN_ROUTE = 'EN-ROUTE'
    OCEANIC  = 'OCEANIC'
    ARRIVAL  = 'ARRIVAL'

    CHOICES = (
        (AIRPORT_RAMP, 'Airport (ramp)'),
        (TAKE_OFF, 'Take Off'),
        (DEPARTURE, 'Departure'),
        (EN_ROUTE, 'En-route'),
        (OCEANIC, 'Oceanic'),
        (ARRIVAL, 'Arrival'),
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True)


    class Meta:
        verbose_name = 'flight phase category'
        verbose_name_plural = 'flight phases categories'

    def __str__(self):
        return self.name


class StakeholderCategory(models.Model):
    AIRPORT_OPERATOR = 'AIRPORT OPERATOR'
    AIRSPACE_USER = 'AIRSPACE USER'
    ANSP = 'ANSP'
    NETWORK_MANAGER  = 'NETWORK MANAGER'

    CHOICES = (
        (AIRPORT_OPERATOR, 'Airport Operator'),
        (AIRSPACE_USER, 'Airspace User'),
        (ANSP, 'ANSP'),
        (NETWORK_MANAGER, 'Network Manager'),
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True)

    class Meta:
        verbose_name = 'stakeholder category'
        verbose_name_plural = 'stakeholder categories'

    def __str__(self):
        return self.name


class RegionCategory(models.Model):
    AFRICA = 'AFRICA'
    ASIA = 'ASIA'
    EUROPE = 'EUROPE'
    GLOBAL  = 'GLOBAL'
    NORTH_AMERICA = 'NORTH AMERICA'
    OCEANIA = 'OCEANIA'
    SOUTH_AMERICA = 'SOUTH AMERICA'

    CHOICES = (
        (AFRICA, 'Africa'),
        (ASIA, 'Asia'),
        (EUROPE, 'Europe'),
        (GLOBAL , 'Global'),
        (NORTH_AMERICA, 'North America'),
        (OCEANIA, 'Oceania'),
        (SOUTH_AMERICA, 'South America'),
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True)

    class Meta:
        verbose_name = 'region category'
        verbose_name_plural = 'region categories'

    def __str__(self):
        return self.name
