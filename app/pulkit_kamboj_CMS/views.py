from django.shortcuts import render
from .models import Contacts


# Create your views here.
def home(request):
    all_contacts = Contacts.objects.all()
    return render(request, 'home.html', {'all_contacts': all_contacts})


def about(request):
    return render(request, 'about.html', {})
