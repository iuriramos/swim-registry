from drf_writable_nested import WritableNestedModelSerializer
from registry.models.technical_interface import TechnicalInterface
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
from .implementation import ImplementationStatusCategorySerializer
from .implementation import ImplementationMaturityCategorySerializer
from .registration_status_category import RegistrationStatusCategorySerializer
from .data_category import DataCategorySerializer
from .activity_category import ActivityCategorySerializer
from .stakeholder_category import StakeholderCategorySerializer
from .region_category import RegionCategorySerializer
from .flight_phase_category import FlightPhaseCategorySerializer

# Serializers define the API representation.
class TechnicalInterfaceSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="registry:technicalinterface-detail")
    # infrastructure_reference_documents = models.ManyToManyField('registry.InfrastructureReferenceDocument', related_name='technical_interfaces', blank=True, verbose_name=_('infrastructure reference documents'))
    # data_standards = models.ManyToManyField('registry.DataStandard', related_name='technical_interfaces', blank=True, verbose_name=_('data standards'))
    # infrastructure_profile = models.ForeignKey('registry.InfrastructureProfile', related_name='technical_interfaces', null=True, blank=True, verbose_name=_('infrastructure profile'))
    
    # infrastructure description
    # data exchange formats
    # end points
    
    class Meta:
        model = TechnicalInterface
        # exclude = ('image', 'infrastructure_profile', 'service', 'infrastructure_reference_documents', 'data_standards', )
        fields = ('pk', 'url', 'description', 'created', 'modified', 'version', )


# ViewSets define the view behavior.
class TechnicalInterfaceViewSet(viewsets.ModelViewSet):
    queryset = TechnicalInterface.objects.all()
    serializer_class = TechnicalInterfaceSerializer

