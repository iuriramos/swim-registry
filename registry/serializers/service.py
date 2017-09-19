from registry.models.service import Service
from rest_framework import serializers, viewsets
from .version_category import VersionCategorySerializer
from .implementation import ImplementationStatusCategorySerializer
from .implementation import ImplementationMaturityCategorySerializer
from .registration_status_category import RegistrationStatusCategorySerializer
from .data_category import DataCategorySerializer
from .activity_category import ActivityCategorySerializer
from .stakeholder_category import StakeholderCategorySerializer
from .region_category import RegionCategorySerializer
from .flight_phase_category import FlightPhaseCategorySerializer


# Serializers define the API representation.
class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="registry:service-detail")
    version_category = VersionCategorySerializer()
    implementation_status = ImplementationStatusCategorySerializer()
    implementation_maturity = ImplementationMaturityCategorySerializer()
    registration_status = RegistrationStatusCategorySerializer()
    data_categories = DataCategorySerializer()
    activity_categories = ActivityCategorySerializer()
    stakeholders = StakeholderCategorySerializer()
    regions = RegionCategorySerializer()
    flight_phases = FlightPhaseCategorySerializer()

    class Meta:
        model = Service
        exclude = ('image', 'organization',)
        

# ViewSets define the view behavior.
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer