from rest_framework import serializers, viewsets
from community.models.participant import Participant
from community.models.participant_category import ParticipantCategory


class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    # image = models.ImageField(upload_to = 'participants/profiles/images/', default = 'participants/profiles/images/none/default.svg', verbose_name=_('image'))
    # reviewed = models.BooleanField(default=False, verbose_name=_('reviewed'))
    url = serializers.HyperlinkedIdentityField(view_name="registry:participant-detail")
    category = serializers.PrimaryKeyRelatedField(queryset=ParticipantCategory.objects.all())
    
    class Meta:
        model = Participant
        fields = ('pk', 'url', 'name', 'created', 'modified', 'description', 'website', 'category', )


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
