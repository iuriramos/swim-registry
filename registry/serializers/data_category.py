from registry.models.data_category import DataCategory
from rest_framework import serializers, viewsets


class DataCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataCategory
        fields = ('pk', 'name', )


class DataCategoryViewSet(viewsets.ModelViewSet):
    queryset = DataCategory.objects.all()
    serializer_class = DataCategorySerializer

