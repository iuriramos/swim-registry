from registry.models.activity_category import ActivityCategory
from rest_framework import serializers, viewsets


# Serializers define the API representation.
class ActivityCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActivityCategory
        fields = ('name', )

# ViewSets define the view behavior.
class ActivityCategoryViewSet(viewsets.ModelViewSet):
    queryset = ActivityCategory.objects.all()
    serializer_class = ActivityCategorySerializer

