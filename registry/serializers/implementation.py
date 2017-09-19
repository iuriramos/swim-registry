from registry.models.implementation import ImplementationStatusCategory, ImplementationMaturityCategory
from rest_framework import serializers, viewsets


# Serializers define the API representation.
class ImplementationStatusCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImplementationStatusCategory
        fields = ('name', )

# ViewSets define the view behavior.
class ImplementationStatusCategoryViewSet(viewsets.ModelViewSet):
    queryset = ImplementationStatusCategory.objects.all()
    serializer_class = ImplementationStatusCategorySerializer


# Serializers define the API representation.
class ImplementationMaturityCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImplementationMaturityCategory
        fields = ('name', )


# ViewSets define the view behavior.
class ImplementationMaturityCategoryViewSet(viewsets.ModelViewSet):
    queryset = ImplementationMaturityCategory.objects.all()
    serializer_class = ImplementationMaturityCategorySerializer
