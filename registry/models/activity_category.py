from django.db import models
from django.utils.translation import ugettext_lazy as _


class ActivityCategory(models.Model):
    AERONAUTICAL_INFORMATION_MANAGEMENT = 'AERONAUTICAL INFORMATION MANAGEMENT'
    AIRPORT_CDM = 'AIRPORT CDM'
    COLLISION_AVOIDANCE = 'COLLISION AVOIDANCE'
    SURVEILLANCE_INFRASTRUCTURE = 'SURVEILLANCE INFRASTRUCTURE'
    TRAFFIC_SEQUENCING = 'TRAFFIC SEQUENCING'
    TRAFFIC_SYNCHRONISATION = 'TRAFFIC SYNCHRONISATION'
    TRAJECTORY_EXECUTION_AND_CONFORMANCE_MONITORING = 'TRAJECTORY EXECUTION AND CONFORMANCE MONITORING'
    CNS_INFRASTRUCTURE = 'CNS INFRASTRUCTURE'
    FLIGHT_INFORMATION_MANAGEMENT = 'FLIGHT INFORMATION MANAGEMENT'
    NAVIGTION_INFRASTRUCTURE = 'NAVIGTION INFRASTRUCTURE'
    ROUTE_DESIGN = 'ROUTE DESIGN'
    SEPARATION_PROVISION = 'SEPARATION PROVISION'
    TRAJECTORY_PLANNING = 'TRAJECTORY PLANNING'
    AIRSPACE_AND_SURFACE_STRUCTURE_DESIGN = 'AIRSPACE AND SURFACE STRUCTURE DESIGN'
    ATM_INFORMATION_MANAGEMENT = 'ATM INFORMATION MANAGEMENT'
    COMMUNICATION_INFRASTRUCTURE = 'COMMUNICATION INFRASTRUCTURE'
    METEOROLOGICAL_INFORMATION = 'METEOROLOGICAL INFORMATION'
    ROUTE_ASSIGNMENT_AND_GUIDANCE = 'ROUTE ASSIGNMENT AND GUIDANCE'
    AIRSPACE_AND_SURFACE_STRUCTURE_ALLOCATION = 'AIRSPACE AND SURFACE STRUCTURE ALLOCATION'
    MET_INFORMATION_MANAGEMENT = 'MET INFORMATION MANAGEMENT'
    AIRSPACE_ACCESS = 'AIRSPACE ACCESS'
    SHARED_INFORMATION_SERVICE_MANAGEMENT  = 'SHARED INFORMATION SERVICE MANAGEMENT'
    DEMAND_AND_CAPACITY_BALANCING = 'DEMAND AND CAPACITY BALANCING'
    CONFLICT_MANAGEMENT = 'CONFLICT MANAGEMENT'
    AIRPORT_MANAGEMENT = 'AIRPORT MANAGEMENT'
    TRAJECTORY_MANAGEMENT = 'TRAJECTORY MANAGEMENT'
    ATM_NETWORK_MANAGEMENT = 'ATM NETWORK MANAGEMENT'

    CHOICES = (
        (AERONAUTICAL_INFORMATION_MANAGEMENT, _('Aeronautical Information Management')),
        (AIRPORT_CDM, _('Airport CDM')),
        (COLLISION_AVOIDANCE, _('Collision Avoidance')),
        (SURVEILLANCE_INFRASTRUCTURE, _('Surveillance Infrastructure')),
        (TRAFFIC_SEQUENCING, _('Traffic Sequencing')),
        (TRAFFIC_SYNCHRONISATION, _('Traffic Synchronisation')),
        (TRAJECTORY_EXECUTION_AND_CONFORMANCE_MONITORING, _('Trajectory Execution And Conformance Monitoring')),
        (CNS_INFRASTRUCTURE, _('CNS Infrastructure')),
        (FLIGHT_INFORMATION_MANAGEMENT, _('Flight Information Management')),
        (NAVIGTION_INFRASTRUCTURE, _('Navigtion Infrastructure')),
        (ROUTE_DESIGN, _('Route Design')),
        (SEPARATION_PROVISION, _('Separation Provision')),
        (TRAJECTORY_PLANNING, _('Trajectory Planning')),
        (AIRSPACE_AND_SURFACE_STRUCTURE_DESIGN, _('Airspace And Surface Structure Design')),
        (ATM_INFORMATION_MANAGEMENT, _('ATM Information Management')),
        (COMMUNICATION_INFRASTRUCTURE, _('Communication Infrastructure')),
        (METEOROLOGICAL_INFORMATION, _('Meteorological Information')),
        (ROUTE_ASSIGNMENT_AND_GUIDANCE, _('Route Assignment And Guidance')),
        (AIRSPACE_AND_SURFACE_STRUCTURE_ALLOCATION, _('Airspace And Surface Structure Allocation')),
        (MET_INFORMATION_MANAGEMENT, _('MET Information Management')),
        (AIRSPACE_ACCESS, _('Airspace Access')),
        (SHARED_INFORMATION_SERVICE_MANAGEMENT , _('Shared Information Service Management')),
        (DEMAND_AND_CAPACITY_BALANCING, _('Demand And Capacity Balancing')),
        (CONFLICT_MANAGEMENT, _('Conflict Management')),
        (AIRPORT_MANAGEMENT, _('Airport Management')),
        (TRAJECTORY_MANAGEMENT, _('Trajectory Management')),
        (ATM_NETWORK_MANAGEMENT, _('ATM Network Management')),
    )

    name = models.CharField(max_length=50, choices=CHOICES, unique=True, verbose_name=_('name'))

    class Meta:
        verbose_name = _('ATM activity category')
        verbose_name_plural = _('ATM activity categories')


    def __str__(self):
        return self.name
