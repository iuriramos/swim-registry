from registry.models.data_exchange_format import DataExchangeFormatService
from rest_framework import serializers, viewsets


class DataExchangeFormatServiceSerializer(serializers.HyperlinkedModelSerializer):
    # image = models.ImageField(upload_to = 'infrastructure/data_exchange_formats/profiles/images/', default = 'infrastructure/data_exchange_formats/profiles/images/none/default.svg', verbose_name=_('image'))
    # infrastructure_reference_documents = models.ManyToManyField('registry.InfrastructureReferenceDocument', blank=True, verbose_name=_('infrastructure reference documents'))
    
    class Meta:
        model = DataExchangeFormatService
        fields = ('pk', 'name', 'created', 'modified', 'description', 'version', )


class DataExchangeFormatServiceViewSet(viewsets.ModelViewSet):
    queryset = DataExchangeFormatService.objects.all()
    serializer_class = DataExchangeFormatServiceSerializer
