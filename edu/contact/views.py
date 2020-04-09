from django.shortcuts import render , redirect
from .forms import ContactForm
from django.contrib import messages
# Create your views here.
from .models import ContactDetails
from django.core.mail import  BadHeaderError
from django.core.mail import send_mail as send_email
from django.http import HttpResponse , HttpResponseRedirect



def send_mail(request):
    contactdetails = ContactDetails.objects.last()
    template = 'contact/contact.html'

    if request.method == 'POST' : 
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            # name = contact_form.cleaned_data['name']
            from_email = contact_form.cleaned_data['from_email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']

            try : 
                send_email( from_email , subject , message , ['test@gmail.com'])
            
            except BadHeaderError : 
                messages.add_message(request, messages.ERROR, 'Ivalid header')

            messages.add_message(request, messages.SUCCESS, 'Message Sent Successfully')
            return HttpResponseRedirect('/')

    else:
        contact_form = ContactForm()


    context = {
        'contactdetails' : contactdetails  , 
        'contact_form' : contact_form
    }

    return render(request, template , context)
