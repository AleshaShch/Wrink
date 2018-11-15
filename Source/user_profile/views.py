from django.shortcuts import render
from django.contrib import messages
from home.views import check_authentication as authenticated
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def profile_page(request, profile_id):
    context = authenticated(request)
    if request.method == 'POST' and 'save' in request.POST:
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        try:
            user = User.objects.get(pk=profile_id)
        except ObjectDoesNotExist:
            return render(request, 'home/home_page.html', context)
        else:
            context['user'] = user
    return render(request, 'profile/profile_page.html', context)
