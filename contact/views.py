from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Contact

def contact_form(request):
    """ A view to display contact page and handle form data """
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(email=email, message=message, new_message=True)
        return redirect('contact_success')
    return render(request, 'contact/contact_form.html')

def contact_success(request):
    """ A view to display contact success page """
    return render(request, 'contact/contact_success.html')
