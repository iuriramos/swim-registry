from registry.models.region_category import RegionCategory
from rest_framework import serializers, viewsets


# Serializers define the API representation.
class RegionCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RegionCategory
        fields = ('name', )

# ViewSets define the view behavior.
class RegionCategoryViewSet(viewsets.ModelViewSet):
    queryset = RegionCategory.objects.all()
    serializer_class = RegionCategorySerializer

