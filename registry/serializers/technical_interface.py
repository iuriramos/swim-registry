from rest_framework import serializers, viewsets
from drf_writable_nested import WritableNestedModelSerializer
from registry.models.technical_interface import TechnicalInterface
from registry.models.data_standard import DataStandard
from registry.models.infrastructure import InfrastructureProfile
from .infrastructure import InfrastructureProfileSerializer, InfrastructureDescriptionSerializer
from .data_standard import DataStandardSerializer
from .data_exchange_format import DataExchangeFormatServiceSerializer
from .end_point import EndPointSerializer


class TechnicalInterfaceSerializer(WritableNestedModelSerializer):
    # infrastructure_reference_documents = models.ManyToManyField('registry.InfrastructureReferenceDocument', related_name='technical_interfaces', blank=True, verbose_name=_('infrastructure reference documents'))
    # data_standards = models.ManyToManyField('registry.DataStandard', related_name='technical_interfaces', blank=True, verbose_name=_('data standards'))
    url = serializers.HyperlinkedIdentityField(view_name="registry:technicalinterface-detail")
    infrastructure_profile = serializers.PrimaryKeyRelatedField(queryset=InfrastructureProfile.objects.all())
    data_standards = serializers.PrimaryKeyRelatedField(many=True, queryset=DataStandard.objects.all())
    # infrastructure_profile = InfrastructureProfileSerializer(read_only=True)
    # data_standards = DataStandardSerializer(many=True, read_only=True)
    infrastructure_description = InfrastructureDescriptionSerializer(allow_null=True)
    data_exchange_formats = DataExchangeFormatServiceSerializer(many=True)
    end_points = EndPointSerializer(many=True)
    
    class Meta:
        model = TechnicalInterface
        fields = ('pk', 'url', 'description', 'created', 'modified', 'version', 'infrastructure_profile', 'data_standards', 'infrastructure_description', 'data_exchange_formats', 'end_points', )


class TechnicalInterfaceViewSet(viewsets.ModelViewSet):
    queryset = TechnicalInterface.objects.all()
    serializer_class = TechnicalInterfaceSerializer

