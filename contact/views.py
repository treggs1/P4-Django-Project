from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Contact

def contact_form(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(email=email, message=message, new_message=True)
        return redirect('contact')
    return render(request, 'contact/contact_form.html')
