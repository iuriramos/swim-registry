from registry.models.flight_phase_category import FlightPhaseCategory
from rest_framework import serializers, viewsets


# Serializers define the API representation.
class FlightPhaseCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FlightPhaseCategory
        fields = ('name', )

# ViewSets define the view behavior.
class FlightPhaseCategoryViewSet(viewsets.ModelViewSet):
    queryset = FlightPhaseCategory.objects.all()
    serializer_class = FlightPhaseCategorySerializer