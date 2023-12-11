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


def details(request, contact_id):
    curr_contact = Contacts.objects.get(pk=contact_id)
    print(curr_contact)
    return render(request, 'details.html', {'curr_contact': curr_contact})


def update(request, contact_id):
    if request.method == 'POST':
        curr_contact = Contacts.objects.get(pk=contact_id)
        form = ContactForm(request.POST or None, instance=curr_contact)
        print(curr_contact.contact_notes)
        curr_email = curr_contact.contact_email
        if form.is_valid():
            print(form["contact_name"].value(), curr_contact.contact_name)
            print(form["contact_email"].value(), curr_contact.contact_email)
            print(form["contact_notes"].value(), curr_contact.contact_notes)
            if Contacts.objects.filter(contact_email=form['contact_email'].value(),
                                       contact_name=form['contact_name'].value(),
                                       contact_notes=form['contact_notes'].value()):
                messages.success(request,
                                 'Contact already exists! Nothing updated in the existing contact.')
                return redirect('home')
            elif curr_email == form['contact_email'].value():
                form.save()
                messages.success(request, 'Contact updated successfully!')
                return redirect('home')
            elif Contacts.objects.filter(contact_email=form['contact_email'].value()):
                messages.success(request,
                                 'Another contact with this e-mail id exists already! Unable to update contact.')
                return render(request, 'update.html',
                              {'curr_contact': curr_contact, 'created_time': curr_contact.created_time})
            else:
                form.save()
                messages.success(request, 'Contact updated successfully!')
                return redirect('home')
    else:
        curr_contact = Contacts.objects.get(pk=contact_id)
        return render(request, 'update.html', {'curr_contact': curr_contact, 'created_time': update_time()})


def delete(request, contact_id):
    curr_contact = Contacts.objects.get(pk=contact_id)
    curr_contact.delete()
    return redirect('home')


def delete_conf(request, contact_id):
    curr_contact = Contacts.objects.get(pk=contact_id)
    return render(request, 'deleteConf.html', {'curr_contact': curr_contact})
