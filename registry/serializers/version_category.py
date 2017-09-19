from registry.models.version_category import VersionCategory
from rest_framework import serializers, viewsets


# Serializers define the API representation.
class VersionCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VersionCategory
        fields = ('name', )

# ViewSets define the view behavior.
class VersionCategoryViewSet(viewsets.ModelViewSet):
    queryset = VersionCategory.objects.all()
    serializer_class = VersionCategorySerializer
