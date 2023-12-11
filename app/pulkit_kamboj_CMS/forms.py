from django import forms
from .models import Contacts


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ["contact_name", "contact_email", "contact_notes", "created_time"]
