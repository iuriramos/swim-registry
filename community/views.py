from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required

from registry.models import DataCategory, ActivityCategory, FlightPhaseCategory, StakeholderCategory, RegionCategory, SubscriptionContentType

from .forms import ProfileForm, RegistrationRequestForm
from .models import Profile, Participant
from .templates.community.success import REGISTRATION_SUCCESSFUL


class RegisterAccountView(View):
    '''View de registro do usuário'''
    template_name = 'community/register.html'

    def get(self, request):
        form = RegistrationRequestForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistrationRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, REGISTRATION_SUCCESSFUL)
            return redirect('community:register')
        return render(request, self.template_name, {'form': form})


def get_profile(request):
     return request.user.profile


@login_required
def profile_edit(request):
    profile = get_profile(request)
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            # save user information
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            # send information message
            messages.add_message(request, messages.INFO, 'Profile settings updated successfully')
            return redirect('community:profile')
    else:
        form =ProfileForm(instance=profile)
    return render(request, 'community/profile.html', {'form': form})


def subscription_tuples(objects, subscribed_items):
    tuples = []
    for item in objects:
        if subscribed_items.filter(pk=item.pk).exists():
            tuples.append((item, True))
        else:
            tuples.append((item, False))
    return tuples

def subscribe_categories(data, objects, subscribed_items):
    for item in objects:
        if data.get(item.name) and not subscribed_items.filter(name=item.name).exists():
            subscribed_items.add(item)
        elif not data.get(item.name) and subscribed_items.filter(name=item.name).exists():
            subscribed_items.remove(item)

@login_required
def subscriptions(request):
    profile = get_profile(request)
    if request.method == 'POST':
        subscribe_categories(request.POST, RegionCategory.objects.all(), profile.subscriptions_region)
        subscribe_categories(request.POST, DataCategory.objects.all(), profile.subscriptions_data)
        subscribe_categories(request.POST, ActivityCategory.objects.all(), profile.subscriptions_activity)
        subscribe_categories(request.POST, FlightPhaseCategory.objects.all(), profile.subscriptions_flight_phase)
        subscribe_categories(request.POST, StakeholderCategory.objects.all(), profile.subscriptions_stakeholder)
        subscribe_categories(request.POST, SubscriptionContentType.objects.all(), profile.subscriptions_content_type)
        return redirect('community:subscriptions')
    else:
        regions = subscription_tuples(RegionCategory.objects.all(), profile.subscriptions_region)
        data = subscription_tuples(DataCategory.objects.all(), profile.subscriptions_data)
        activities = subscription_tuples(ActivityCategory.objects.all(), profile.subscriptions_activity)
        flight_phases = subscription_tuples(FlightPhaseCategory.objects.all(), profile.subscriptions_flight_phase)
        stakeholders = subscription_tuples(StakeholderCategory.objects.all(), profile.subscriptions_stakeholder)
        content_types = subscription_tuples(SubscriptionContentType.objects.all(), profile.subscriptions_content_type)
        return render(request, 'community/subscriptions.html', {
                        'regions': regions, 'data': data, 'activities': activities,
                        'flight_phases': flight_phases, 'stakeholders': stakeholders,
                        'content_types': content_types
                    })


@login_required
def organizations_all(request):
    organizations = Participant.objects.all()
    return render(request, 'community/organizations.html', {'organizations': organizations})


@login_required
def organization(request, pk):
    organization = get_object_or_404(Participant, pk=pk)
    return render(request, 'community/organization.html', {'organization': organization})


# @login_required
# def organization_list(request):
#     profile = get_profile(request)
#     organizations = profile.organizations
#     return render(request, 'community/organizations_list.html', {'organizations': organizations})


# @login_required
# def organization_new(request):
#     profile = get_profile(request)


# # TODO: Support permissions and groups
# @login_required
# def organization_edit(request, pk):
#     user = request.user
#     profile = get_profile(request)
#     organization = get_object_or_404(Organization, pk=pk)
#     if request.method == 'POST':
#         form = OrganizationForm(request.POST, instance=organization)
#         if form.is_valid():
#             organization = form.save()
#             messages.add_message(request, messages.INFO, 'Organization settings updated successfully')
#             return redirect('community:organization')
#     else:
#         form = OrganizationForm(instance=organization)
#     return render(request, 'community/organization_edit.html', {'form': form})


