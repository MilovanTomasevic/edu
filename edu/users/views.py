from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import UserProfile
from django.views.generic import  DetailView, ListView

def profile(request):
    # context = UserProfile.objects.get(user=request.user)
    # return render(request, 'users/profile.html', context)
    return render(request, 'users/profile.html')

@login_required
def update_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('ecenter-profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile_update.html', context)


class ProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'users/profile_detail.html'  #
