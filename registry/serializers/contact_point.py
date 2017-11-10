from registry.models.contact_point import ContactPointService
from rest_framework import serializers, viewsets


class ContactPointServiceSerializer(serializers.HyperlinkedModelSerializer):
    # image = models.ImageField(upload_to = 'services/contact_points/images/', default = 'services/contact_points/images/none/default.svg', blank=True, verbose_name=_('image'))
    class Meta:
        model = ContactPointService
        fields = ('pk', 'name', 'created', 'modified', 'description', 'telephone', 'email',)


class ContactPointServiceViewSet(viewsets.ModelViewSet):
    queryset = ContactPointService.objects.all()
    serializer_class = ContactPointServiceSerializer
