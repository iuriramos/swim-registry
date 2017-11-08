from drf_writable_nested import WritableNestedModelSerializer
from registry.models.service import Service
from registry.models.version_category import VersionCategory
from registry.models.implementation import ImplementationMaturityCategory, ImplementationStatusCategory
from registry.models.registration_status_category import RegistrationStatusCategory
from registry.models.data_category import DataCategory
from registry.models.activity_category import ActivityCategory
from registry.models.stakeholder_category import StakeholderCategory
from registry.models.region_category import RegionCategory
from registry.models.flight_phase_category import FlightPhaseCategory
from rest_framework import serializers, viewsets
from .version_category import VersionCategorySerializer
from .technical_interface import TechnicalInterfaceSerializer
from .implementation import ImplementationStatusCategorySerializer
from .implementation import ImplementationMaturityCategorySerializer
from .registration_status_category import RegistrationStatusCategorySerializer
from .data_category import DataCategorySerializer
from .activity_category import ActivityCategorySerializer
from .stakeholder_category import StakeholderCategorySerializer
from .region_category import RegionCategorySerializer
from .flight_phase_category import FlightPhaseCategorySerializer


# Serializers define the API representation.
class ServiceSerializer(WritableNestedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="registry:service-detail")
    version_category = serializers.PrimaryKeyRelatedField(queryset=VersionCategory.objects.all())
    implementation_status = serializers.PrimaryKeyRelatedField(queryset=ImplementationStatusCategory.objects.all())
    implementation_maturity = serializers.PrimaryKeyRelatedField(queryset=ImplementationMaturityCategory.objects.all())
    registration_status = serializers.PrimaryKeyRelatedField(queryset=RegistrationStatusCategory.objects.all())
    data_categories = serializers.PrimaryKeyRelatedField(many=True, queryset=DataCategory.objects.all())
    activity_categories = serializers.PrimaryKeyRelatedField(many=True, queryset=ActivityCategory.objects.all())
    stakeholders = serializers.PrimaryKeyRelatedField(many=True, queryset=StakeholderCategory.objects.all())
    regions = serializers.PrimaryKeyRelatedField(many=True, queryset=RegionCategory.objects.all())
    flight_phases = serializers.PrimaryKeyRelatedField(many=True, queryset=FlightPhaseCategory.objects.all())
    technical_interface = TechnicalInterfaceSerializer()

    class Meta:
        model = Service
        exclude = ('image', 'organization',)
        # fields = ('version_category', )
        

# ViewSets define the view behavior.
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer