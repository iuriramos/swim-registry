from registry.models.activity_category import ActivityCategory
from rest_framework import serializers, viewsets


class ActivityCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActivityCategory
        fields = ('pk', 'name', )


class ActivityCategoryViewSet(viewsets.ModelViewSet):
    queryset = ActivityCategory.objects.all()
    serializer_class = ActivityCategorySerializer

