from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def get_profile(request):
     return request.user.profile


@login_required
def index(request):
    profile = get_profile(request)
    return render(request, 'registry/index.html', {'profile': profile})

@login_required
def about(request):
    pass
