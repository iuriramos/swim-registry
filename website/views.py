from django.shortcuts import render

def index(request):
    """View que renderiza página principal do website"""
    return render(request, 'index.html')
