from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registry.models.end_point import EndPoint


class EndPointDetailView(DetailView):
    model = EndPoint
    context_object_name = 'end_point'
    template_name = 'registry/end_point_detail.html'
