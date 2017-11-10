from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers, viewsets
from registry.models.infrastructure import InfrastructureDescription, InfrastructureProfile
from registry.models.technical_interface_binding import TechnicalInterfaceBindingProfile
from .technical_interface_binding import TechnicalInterfaceBindingDescriptionSerializer, TechnicalInterfaceBindingProfileSerializer


class InfrastructureProfileSerializer(serializers.HyperlinkedModelSerializer):
    # image = models.ImageField(upload_to = 'infrastructure/profiles/images/', default = 'infrastructure/profiles/images/none/default.svg', verbose_name=_('image'))
    # infrastructure_reference_documents = models.ManyToManyField('registry.InfrastructureReferenceDocument', related_name='infrastructure_profiles', verbose_name=_('infrastructure reference documents'))
    url = serializers.HyperlinkedIdentityField(view_name="registry:infrastructureprofile-detail")
    technical_interface_bindings = serializers.PrimaryKeyRelatedField(many=True, queryset=TechnicalInterfaceBindingProfile.objects.all())
    
    class Meta:
        model = InfrastructureProfile
        fields = ('pk', 'url', 'name', 'created', 'modified', 'description', 'version', 'technical_interface_bindings', )

class InfrastructureProfileViewSet(viewsets.ModelViewSet):
    queryset = InfrastructureProfile.objects.all()
    serializer_class = InfrastructureProfileSerializer


class InfrastructureDescriptionSerializer(WritableNestedModelSerializer):
    # infrastructure_reference_documents = models.ManyToManyField('registry.InfrastructureReferenceDocument', related_name='infrastructure_description', blank=True, verbose_name=_('infrastructure reference documents'))
    # image = models.ImageField(upload_to = 'infrastructure/infrastructure_description/images/', default = 'infrastructure/infrastructure_description/images/none/default.svg', verbose_name=_('image'))
    # infrastructure_documents = models.ManyToManyField(InfrastructureDocument, related_name='infrastructure_description')
    technical_interface_bindings = TechnicalInterfaceBindingDescriptionSerializer(many=True)

    class Meta:
        model = InfrastructureDescription
        fields = ('pk', 'created', 'modified', 'description', 'version', 'technical_interface_bindings', )
    
class InfrastructureDescriptionViewSet(viewsets.ModelViewSet):
    queryset = InfrastructureDescription.objects.all()
    serializer_class = InfrastructureDescriptionSerializer
