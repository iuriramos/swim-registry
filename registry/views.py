from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import RegisterAccountForm
from .models import RegistrationRequest

# Create your views here.

class RegisterAccountView(View):
    template_name = "register.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = RegisterAccountForm(request.POST)

        if form.is_valid():
            data_form = form.data
            #request = RegistrationRequest(**data_form)
            registration_request = RegistrationRequest(
                                first_name=data_form['first_name'],
                                last_name=data_form['last_name'],
                                email=data_form['email'],
                                organization=data_form['organization'],
                                role=data_form['role']
                            )
            registration_request.save()
            return render(request, 'success.html')

        return render(request, self.template_name, {'form': form})

@login_required
def registry_index(request):
    return render(request, 'my_registry.html', {}) # stub method
