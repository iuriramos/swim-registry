from registry.models.end_point import EndPoint
from rest_framework import serializers, viewsets


class EndPointSerializer(serializers.HyperlinkedModelSerializer):
    # image = models.ImageField(upload_to = 'services/end_points/images/', default = 'services/end_points/images/none/default.svg', verbose_name=_('image'))
    
    class Meta:
        model = EndPoint
        fields = ('pk', 'name', 'created', 'modified', 'description', 'address', )


class EndPointViewSet(viewsets.ModelViewSet):
    queryset = EndPoint.objects.all()
    serializer_class = EndPointSerializer