from registry.models.stakeholder_category import StakeholderCategory
from rest_framework import serializers, viewsets


# Serializers define the API representation.
class StakeholderCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StakeholderCategory
        fields = ('name', )

# ViewSets define the view behavior.
class StakeholderCategoryViewSet(viewsets.ModelViewSet):
    queryset = StakeholderCategory.objects.all()
    serializer_class = StakeholderCategorySerializer
