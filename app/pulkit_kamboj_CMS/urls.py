from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('create', views.add_contact, name='createContact'),
    path('details/<contact_id>', views.details, name='details'),
    path('update/<contact_id>', views.update, name='update')
]
