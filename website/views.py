from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

def index(request):
    """View que renderiza página principal do website"""
    return render(request, 'index.html')
