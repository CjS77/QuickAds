from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
import json


class ActiveUserRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_profile.active:
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(
                request, ('Please Login Or May Be Your Account Is Not Active'))
            return redirect('accounts:login')
