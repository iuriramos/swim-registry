from registry.models.technical_interface_binding import TechnicalInterfaceBindingDescription, TechnicalInterfaceBindingProfile
from rest_framework import serializers, viewsets


class TechnicalInterfaceBindingProfileSerializer(serializers.HyperlinkedModelSerializer):
    # image = models.ImageField(upload_to = 'infrastructure/technical_interface_bindings/images/', default = 'infrastructure/technical_interface_bindings/images/none/default.svg', verbose_name=_('image'))
    class Meta:
        model = TechnicalInterfaceBindingProfile
        fields = ('pk', 'name', 'created', 'modified', 'description', )

class TechnicalInterfaceBindingProfileViewSet(viewsets.ModelViewSet):
    queryset = TechnicalInterfaceBindingProfile.objects.all()
    serializer_class = TechnicalInterfaceBindingProfileSerializer


class TechnicalInterfaceBindingDescriptionSerializer(serializers.HyperlinkedModelSerializer):
    # image = models.ImageField(upload_to = 'infrastructure/technical_interface_bindings/images/', default = 'infrastructure/technical_interface_bindings/images/none/default.svg', verbose_name=_('image'))
    class Meta:
        model = TechnicalInterfaceBindingDescription
        fields = ('pk', 'name', 'created', 'modified', 'description', )

class TechnicalInterfaceBindingDescriptionViewSet(viewsets.ModelViewSet):
    queryset = TechnicalInterfaceBindingDescription.objects.all()
    serializer_class = TechnicalInterfaceBindingDescriptionSerializer
