from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required

from .forms import RegistrationRequestForm
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
