from registry.models.registration_status_category import RegistrationStatusCategory
from rest_framework import serializers, viewsets


# Serializers define the API representation.
class RegistrationStatusCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RegistrationStatusCategory
        fields = ('name', )

# ViewSets define the view behavior.
class RegistrationStatusCategoryViewSet(viewsets.ModelViewSet):
    queryset = RegistrationStatusCategory.objects.all()
    serializer_class = RegistrationStatusCategorySerializer