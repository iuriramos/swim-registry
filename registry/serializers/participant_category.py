from rest_framework import serializers, viewsets
from community.models.participant_category import ParticipantCategory


class ParticipantCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ParticipantCategory
        fields = ('pk', 'name', )


class ParticipantCategoryViewSet(viewsets.ModelViewSet):
    queryset = ParticipantCategory.objects.all()
    serializer_class = ParticipantCategorySerializer

