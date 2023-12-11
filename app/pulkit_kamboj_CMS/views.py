from django.shortcuts import render, redirect
from .models import Contacts
from .forms import ContactForm
from django.contrib import messages
from datetime import datetime


# Create your views here.
def home(request):
    all_contacts = Contacts.objects.all()
    return render(request, 'home.html', {'all_contacts': all_contacts})


def about(request):
    return render(request, 'about.html', {})


def update_time():
    created_time = datetime.now().strftime('%b %d, %Y, %H:%M')
    return created_time


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            print(form["contact_email"].value())
            if Contacts.objects.filter(contact_email=form['contact_email'].value()):
                messages.success(request, 'Contact with given e-mail exists already! Unable to add contact.')
                return redirect('addContact')
            else:
                form.save()
                messages.success(request, 'Contact created successfully.')
                return redirect('home')
    else:
        return render(request, 'addContact.html', {'created_time': update_time()})
