from registry.models.data_category import DataCategory
from rest_framework import serializers, viewsets


# Serializers define the API representation.
class DataCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataCategory
        fields = ('name', )

# ViewSets define the view behavior.
class DataCategoryViewSet(viewsets.ModelViewSet):
    queryset = DataCategory.objects.all()
    serializer_class = DataCategorySerializer

