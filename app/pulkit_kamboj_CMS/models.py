from django.db import models


# Create your models here.
class Contacts(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=250)
    contact_notes = models.CharField(max_length=250)
    created_time = models.CharField(max_length=25)

    def __str__(self):
        return self.contact_name
