from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import UserProfile
from courses.models import Course
from django.views.generic import  DetailView, ListView

def profile(request):
    courses = Course.objects.filter(teacher=request.user.userprofile)
    if courses.exists():
        context = {
        'courses' : courses,
        }
    else:
        context = None

    return render(request, 'users/profile.html', context)

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
    template_name = 'users/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        courses = Course.objects.filter(teacher__pk=self.kwargs.get('pk'))
        context.update({
            'courses' : courses,
        })
        return context
