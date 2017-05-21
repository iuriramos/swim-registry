from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .base import get_profile


@login_required
def index_view(request):
    profile = get_profile(request)
    return render(request, 'registry/index.html', {'profile': profile})

