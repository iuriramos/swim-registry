from registry.models.implementation import ImplementationStatusCategory, ImplementationMaturityCategory
from rest_framework import serializers, viewsets


class ImplementationStatusCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImplementationStatusCategory
        fields = ('name', )

class ImplementationStatusCategoryViewSet(viewsets.ModelViewSet):
    queryset = ImplementationStatusCategory.objects.all()
    serializer_class = ImplementationStatusCategorySerializer


class ImplementationMaturityCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImplementationMaturityCategory
        fields = ('name', )

class ImplementationMaturityCategoryViewSet(viewsets.ModelViewSet):
    queryset = ImplementationMaturityCategory.objects.all()
    serializer_class = ImplementationMaturityCategorySerializer
