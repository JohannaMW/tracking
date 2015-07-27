from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models import Driver
from django.forms import ModelForm

class DriverForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = Driver
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
