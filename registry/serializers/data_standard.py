from registry.models.data_standard import DataStandard
from rest_framework import serializers, viewsets


class DataStandardSerializer(serializers.HyperlinkedModelSerializer):
    # image = models.ImageField(upload_to = 'infrastructure/data_standards/profiles/images/', default = 'infrastructure/data_standards/profiles/images/none/default.svg', verbose_name=_('image'))
    # infrastructure_reference_documents = models.ManyToManyField('registry.InfrastructureReferenceDocument', related_name='data_standards', verbose_name=_('infrastructure reference documents'))
    url = serializers.HyperlinkedIdentityField(view_name="registry:datastandard-detail")
    
    class Meta:
        model = DataStandard
        fields = ('pk', 'url', 'name', 'created', 'modified', 'description', 'version', )


class DataStandardViewSet(viewsets.ModelViewSet):
    queryset = DataStandard.objects.all()
    serializer_class = DataStandardSerializer

