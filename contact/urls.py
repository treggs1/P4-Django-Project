from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_form, name='contact_form'),
    path('contact_success/', views.contact_form, name='contact_success'),
    path('contact_success/', views.contact_success, name='contact_success'),
]
