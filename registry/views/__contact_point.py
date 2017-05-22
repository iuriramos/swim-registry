from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from registry.forms.contact_point import ContactPointForm
from .base import get_profile


@login_required
def contact_point_new(request):
    if request.method == 'POST':
        form = ContactPointForm(request.POST)
        if form.is_valid():
            contact_point = form.save()
            pk_service = request.POST['service_id']
            service = Service.objects.get(pk=pk_service)
            service.contact_points.add(contact_point)
            service.save()
            messages.add_message(request, messages.INFO, 'Organization created successfully')
            return redirect('community:profile')
    else:
        form = ContactPointForm()
    return render(request, 'community/organization_edit.html', {'form': form})


@login_required
def contact_point_edit(request):
    user = request.user
    profile = get_profile(request)
    organization = profile.organization
    if request.method == 'POST':
        form = ContactPointForm(request.POST, instance=organization)
        if form.is_valid():
            organization = form.save()
            messages.add_message(request, messages.INFO, 'Organization settings updated successfully')
            return redirect('community:organization')
    else:
        form = ContactPointForm(instance=organization)
    return render(request, 'community/organization_edit.html', {'form': form})
