from django.shortcuts import render
from .models import UserProfile
# Create your views here.
def profile(request):
    # context = UserProfile.objects.get(user=request.user)
    # return render(request, 'users/profile.html', context)
    return render(request, 'users/profile.html')