from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.contrib import messages

def admin_teacher_required(view_func):
    def wrap(request, *args, **kwargs):
        allowed_roles=["admin", "teacher"]
        if request.userprofile.role in allowed_roles:
            return view_func(request, *args, **kwargs)
        else:
            messages.add_message(request, messages.ERROR , 'Denied access')
            return HttpResponseRedirect('/')
            # return HttpResponseRedirect(reverse('func_name'))
    return wrap

def admin_only(view_func):
    def wrap(request, *args, **kwargs):
        if request.userprofile.role == "admin":
            return view_func(request, *args, **kwargs)
        else:
            messages.add_message(request, messages.ERROR , 'Denied access')
            return HttpResponseRedirect('/')
            # return HttpResponseRedirect(reverse('func_name'))
    return wrap
        